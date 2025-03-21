from .sitemap_generator_model import SitemapGenerator, ProjectBrief, Pages
from .sitemap_generator_entity import SitemapGenerator as SitemapGeneratorEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable
import openai
import os
import json
import requests
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.llm_call import get_llm_response
from src.utils.example import PageExamples
from src.utils.logging import logger
import base64
import uuid


openai.api_key = os.environ.get("OPENAI_API_KEY")


@Injectable
class SitemapGeneratorService:
    @async_db_request_handler
    async def add_sitemap_generator(
        self, sitemap_generator: SitemapGenerator, session: AsyncSession
    ):
        new_sitemap_generator = SitemapGeneratorEntity(**sitemap_generator.dict())
        session.add(new_sitemap_generator)
        await session.commit()
        return new_sitemap_generator.id

    @async_db_request_handler
    async def get_sitemap_generator(self, session: AsyncSession):
        query = select(SitemapGeneratorEntity)
        result = await session.execute(query)
        return result.scalars().all()

    # def generate_image(
    #     self,
    #     prompt,
    #     negative_prompt=None,
    #     width=1024,
    #     height=1024,
    #     steps=4,
    #     model="flux1-schnell-fp8.safetensors",
    #     batch_size=1,
    #     cfg=1.0,
    #     sampler_name="euler",
    #     scheduler="simple",
    #     guidance=3.5,
    # ):
    #     url = "http://192.168.0.120:5000/api/generate"
    #     payload = {
    #         "positive_prompt": prompt,
    #         "negative_prompt": negative_prompt,
    #         "width": width,
    #         "height": height,
    #         "steps": steps,
    #         "model": model,
    #         "batch_size": batch_size,
    #         "cfg": cfg,
    #         "sampler_name": sampler_name,
    #         "scheduler": scheduler,
    #         "guidance": guidance,
    #     }

    #     headers = {"Content-Type": "application/json"}
    #     response = requests.post(url, json=payload, headers=headers)
    #     if response.status_code == 200:
    #         data = response.json()
    #         if data.get("success"):
    #             # Return the base64 image data from the first generated image.
    #             return data["images"][0]["base64"]
    #         else:
    #             raise Exception(f"Image generation failed: {data.get('error')}")
    #     else:
    #         raise Exception(f"HTTP error: {response.status_code}")

    # def save_base_64(
    #     self, base64_data, folder="src/assets", image_format="png", filename=None
    # ):
    #     if base64_data.startswith("data:image"):
    #         _, base64_data = base64_data.split(",", 1)

    #     image_data = base64.b64decode(base64_data)
    #     os.makedirs(folder, exist_ok=True)
    #     if filename is None:
    #         filename = f"{uuid.uuid4()}.{image_format}"

    #     else:
    #         if not filename.endswith(f".{image_format}"):
    #             filename = f"{filename}.{image_format}"

    #     file_path = os.path.join(folder, filename)

    #     if os.path.exists(file_path):
    #         os.remove(file_path)

    #     with open(file_path, "wb") as f:
    #         f.write(image_data)

    #     image_url = f"/static/images/{filename}"

    #     return image_url

    async def generate_sitemap_generator(self, data: SitemapGenerator):
       
         
        prompt  = ''' 
                You provide assistance with project brief,
                You understand the business requirement and you are highly skillfull to rewrite the business description that is well detailed and crystal clear to be understand by everyone.
                
           '''
        
        response = get_llm_response(
            user_prompt=f"write a project brief make it understandable {data.business_name}, {data.business_description}",
            system_prompt=prompt,
            response_format= ProjectBrief
        )
        json_project = response.model_dump_json()
        project_brief = json.loads(json_project)
        print('-------------------------------------------')
        print('-------------------------------------------')
    


        sitemap_prompt = '''
                You are a Website Strategist tasked with building a strong website foundation.
                Your goal is to ensure strategic alignment with business objectives through thorough research,data-driven decision-making, and a clear understanding of the business's value proposition.
                Approach each decision with a focus on clarity, usability, and long-term scalability.

                
        '''
        response = get_llm_response(
            user_prompt=f"Generate a sitemap for a website representing the business '{project_brief}'.",
            system_prompt=sitemap_prompt,
            response_format=Pages
        )
        json_res = response.model_dump_json()
        json_loads = json.loads(json_res)





        # hero_prompt = f"Generate a high-quality hero section image for a website representing the business '{data.business_description}. only generate the image Dont generate anyother contents.'."

        # try:
        #     hero_image = self.generate_image(hero_prompt)
        #     hero_image_url = self.save_base_64(
        #         hero_image,
        #         folder="src/images",
        #         image_format="png",
        #         filename="hero_image",
        #     )
        #     json_res["imageUrl"] = hero_image_url
        # except Exception as e:
        #     json_res["imageUrl"] = None
        #     logger.error(e)
        return json_loads, project_brief
