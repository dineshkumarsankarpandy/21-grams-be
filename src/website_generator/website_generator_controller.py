from nest.core import Controller, Get, Post, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config
from src.utils.logging import logger
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException, UploadFile, Form
from .website_generator_service import WebsiteGeneratorService
from .website_generator_model import Sitemap
from dotenv import load_dotenv
import requests
import shutil
import zipfile
import os
import base64
import time
import mimetypes



@Controller("website_generator", tag="website_generator")
class WebsiteGeneratorController:

    def __init__(self, website_generator_service: WebsiteGeneratorService):
        self.website_generator_service = website_generator_service

    @Get("/")
    async def get_website_generator(self, session: AsyncSession = Depends(config.get_db)):
        return await self.website_generator_service.get_website_generator(session)

    @Post("/")
    async def add_website_generator(self, website_generator: Sitemap, session: AsyncSession = Depends(config.get_db)):
        return await self.website_generator_service.add_website_generator(website_generator, session)
    

    
    @Post('/website-generator')

    async def website_generator(self, data: Sitemap):

        try:

            result = await self.website_generator_service.generate_website(data)
            print(result,'<----------------------------')
            return JSONResponse(content =result, status_code=status.HTTP_200_OK)

        except HTTPException as e:

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = f'Internal server error'
                    )
        


    @Post('/deploy-website')
    async def deploy_website(self, sitemap_id: str = Form(...), file: UploadFile = Form(...)):
        load_dotenv()
        vercel_token = os.getenv("VERCEL_TOKEN")
        if not vercel_token:
            logger.error("Vercel token not found in .env")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Vercel token not found in .env"
            )

        headers = {
            "Authorization": f"Bearer {vercel_token}",
            "Content-Type": "application/json"
        }
        temp_dir = "temp"
        extract_dir = os.path.join(temp_dir, f"extracted_{sitemap_id}")
        temp_zip_path = os.path.join(temp_dir, f"website_{sitemap_id}.zip")

        os.makedirs(temp_dir, exist_ok=True)

        try:
            # Save the uploaded zip file
            logger.info(f"Saving uploaded file to {temp_zip_path}")
            with open(temp_zip_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Extract the zip file
            logger.info(f"Extracting zip to {extract_dir}")
            os.makedirs(extract_dir, exist_ok=True)
            with zipfile.ZipFile(temp_zip_path, "r") as zip_ref:
                zip_ref.extractall(extract_dir)

            # Prepare files for Vercel deployment
            files_payload = []
            for root, _, files in os.walk(extract_dir):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(file_path, extract_dir)
                    mime_type, _ = mimetypes.guess_type(file_path)
                    is_text = mime_type is not None and mime_type.startswith("text")
                    
                    if is_text:
                        with open(file_path, "r", encoding="utf-8") as f:
                            file_content = f.read()
                        content_to_send = file_content  # send plain text for text files
                    else:
                        # For binary files, read in binary mode and base64 encode
                        with open(file_path, "rb") as f:
                            file_content = f.read()
                        content_to_send = base64.b64encode(file_content).decode("utf-8")
                    
                    logger.debug(f"File: {relative_path}, Content sample: {content_to_send[:50]}...")
                    files_payload.append({
                        "file": relative_path,
                        "data": content_to_send
                    })

            logger.info(f"Deploying files to Vercel for sitemap_id: {sitemap_id}")
            payload = {
                "name": f"user-website-{sitemap_id}",
                "files": files_payload,
                "projectSettings": {"framework": None},
                "public": True
            }

            response = requests.post(
                "https://api.vercel.com/v13/deployments",
                headers=headers,
                json=payload
            )

            logger.debug(f"Vercel response status: {response.status_code}")
            logger.debug(f"Vercel response text: {response.text}")

            if response.status_code == 200:
                deployment_url = response.json().get("url")
                deployment_id = response.json().get("id")
                project_id = response.json().get("projectId")

                if not deployment_url or not deployment_id:
                    logger.error("No deployment URL or ID in response")
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="No deployment URL or ID returned"
                    )

                # Wait for deployment to be ready
                max_attempts = 30  # Wait up to 5 minutes (30 * 10s)
                for attempt in range(max_attempts):
                    status_response = requests.get(
                        f"https://api.vercel.com/v13/deployments/{deployment_id}",
                        headers=headers
                    )
                    if status_response.status_code == 200:
                        status_data = status_response.json()
                        ready_state = status_data.get("readyState")
                        logger.debug(f"Deployment status: {ready_state}")
                        if ready_state == "READY":
                            break
                        elif ready_state in ["ERROR", "CANCELED"]:
                            logger.error(f"Deployment failed: {status_data}")
                            raise HTTPException(
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Deployment failed: {status_data.get('error', 'Unknown error')}"
                            )
                    time.sleep(10)  # Wait 10 seconds before next check
                else:
                    logger.error("Deployment not ready after max attempts")
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="Deployment not ready after max attempts"
                    )

                # Assign alias
                alias_payload = {
                    "domain": f"user-website-{sitemap_id}.vercel.app",
                    "deploymentId": deployment_id  # Explicitly map alias to this deployment
                }
                alias_response = requests.post(
                    f"https://api.vercel.com/v10/projects/{project_id}/alias",
                    headers=headers,
                    json=alias_payload
                )

                if alias_response.status_code != 200:
                    logger.error(f"Failed to assign alias: {alias_response.text}")
                    # Fallback to deployment URL if alias fails
                    return JSONResponse(
                        content={"deployment_url": f"https://{deployment_url}"},
                        status_code=status.HTTP_200_OK
                    )
                else:
                    logger.info(f"Alias assigned: {alias_payload['domain']}")

                logger.info(f"Deployment successful: https://{deployment_url}")
                return JSONResponse(
                    content={"deployment_url": f"https://user-website-{sitemap_id}.vercel.app"},
                    status_code=status.HTTP_200_OK
                )
            else:
                logger.error(f"Vercel API error: {response.status_code} - {response.text}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Vercel API error: {response.status_code} - {response.text}"
                )
        except Exception as e:
            logger.error(f"Deployment exception: {str(e)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error during deployment: {str(e)}"
            )
        finally:
            if os.path.exists(temp_zip_path):
                logger.info(f"Cleaning up: {temp_zip_path}")
                os.remove(temp_zip_path)
            if os.path.exists(extract_dir):
                logger.info(f"Cleaning up: {extract_dir}")
                shutil.rmtree(extract_dir)