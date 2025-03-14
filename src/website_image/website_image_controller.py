from nest.core import Controller, Get, Post, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
from .website_image_service import WebsiteImageService
from .website_image_model import WebsiteImage
from src.utils.logging import logger

@Controller("website_image", tag="website_image")
class WebsiteImageController:

    def __init__(self, website_image_service: WebsiteImageService):
        self.website_image_service = website_image_service

    @Get("/")
    async def get_website_image(self, session: AsyncSession = Depends(config.get_db)):
        return await self.website_image_service.get_website_image(session)

    @Post("/")
    async def add_website_image(self, website_image: WebsiteImage, session: AsyncSession = Depends(config.get_db)):
        return await self.website_image_service.add_website_image(website_image, session)
    

    @Post("/image-website")
    async def generate_website_by_img(self, data:WebsiteImage):  # Adjust based on your actual data model
        try:
            logger.info("Received request with payload: %s", data)
            generated_code = await self.website_image_service.generate_website_img(data)
            logger.info("Generated code: %s", generated_code)
            return JSONResponse(content={"code": generated_code}, status_code=status.HTTP_200_OK)
        except Exception as e:
            logger.error("Error in generate_website_by_img: %s", str(e))
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}"
            )
            
        
 