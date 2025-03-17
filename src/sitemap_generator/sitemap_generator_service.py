from .sitemap_generator_model import SitemapGenerator
from .sitemap_generator_entity import SitemapGenerator as SitemapGeneratorEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable
import openai
from agents import Agent
import os
import json
import requests
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.llm_call import get_llm_response
from src.utils.example import PageExamples
import base64
import uuid


openai.api_key = os.environ.get("OPENAI_API_KEY")

@Injectable
class SitemapGeneratorService:
    
    @async_db_request_handler
    async def add_sitemap_generator(self, sitemap_generator: SitemapGenerator, session: AsyncSession):
        new_sitemap_generator = SitemapGeneratorEntity(**sitemap_generator.dict())
        session.add(new_sitemap_generator)
        await session.commit()
        return new_sitemap_generator.id

    @async_db_request_handler
    async def get_sitemap_generator(self, session: AsyncSession):
        query = select(SitemapGeneratorEntity)
        result = await session.execute(query)
        return result.scalars().all()
    

    def generate_image(self, prompt, negative_prompt = None, width= 1024, height=1024, 
                       steps=4, model = "flux1-schnell-fp8.safetensors",batch_size =1,
                       cfg=1.0, sampler_name="euler", scheduler="simple", guidance=3.5 
                       
                       ):
         
        
         url = "http://192.168.0.120:5000/api/generate"
         payload = {
            "positive_prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "steps": steps,
            "model": model,
            "batch_size": batch_size,
            "cfg": cfg,
            "sampler_name": sampler_name,
            "scheduler": scheduler,
            "guidance": guidance
        }
         
         headers = {"Content-Type": "application/json"}
         response =  requests.post(url, json=payload, headers=headers)
         if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                # Return the base64 image data from the first generated image.
                return data["images"][0]["base64"]
            else:
                raise Exception(f"Image generation failed: {data.get('error')}")
         else:
            raise Exception(f"HTTP error: {response.status_code}")
         
    
    def save_base_64(self, base64_data, folder = "src/assets", image_format = "png",filename = None):

        if base64_data.startswith("data:image"):
            _,base64_data = base64_data.split(",",1)
        
        image_data = base64.b64decode(base64_data)
        os.makedirs(folder,exist_ok=True)
        if filename is None:
            filename = f"{uuid.uuid4()}.{image_format}"

        
        else:
            if not filename.endswith(f".{image_format}"):
                filename = f"{filename}.{image_format}"

        file_path = os.path.join(folder,filename)
        
        if os.path.exists(file_path):
            os.remove(file_path)
        
        with open(file_path,"wb") as f:
            f.write(image_data)

        image_url = f"/static/images/{filename}"

        return image_url
    



    async def generate_sitemap_generator(self, data: SitemapGenerator):

        output_json =  '''{
            "businessName:" "users business name here...",
            "businessDescription:" "users description here..."
            "pages":[
            "pageTitle": "Home", 
            "sections": [
                {
                "sectionTitle": "section title here.......",
                "sectionDescription": "sections Description here...."
                }

            ]

            ]
            }'''
        

        prompt = f"""
    You are a Business Analyst in a website design project. Your role is to ensure the website’s structure aligns with the client’s business goals, functional requirements, and user needs. Specifically, you are responsible for identifying or generating the website’s sitemap.

         Here's how you should approach your task:

        1. **Gather and Document Key Information:**
           - Conduct **client interviews** and workshops to understand business goals, target audience, and functional requirements.
           - Collaborate with stakeholders (e.g., marketing, sales teams) to identify internal requirements.
           - Work with UX designers and content strategists to understand user needs and ensure the site structure enhances the user experience.
           - Conduct a **content inventory** if necessary, especially for website redesigns.

        2. **Ensure Sitemap Aligns with Business Goals and User Needs:**
           - Map **business goals** (e.g., lead generation, product promotion) to specific pages and content in the sitemap.
           - Ensure the sitemap accommodates **optimal user flows**, ensuring users can easily navigate and meet their goals.
           - Use iterative feedback from stakeholders to refine the sitemap.
           - Prioritize **key pages** and ensure high-priority content is accessible.

        3. **Collaborate with Other Team Members:**
           - Work with **UX designers** to ensure the sitemap reflects smooth user navigation.
           - Collaborate with **content strategists** to ensure content is logically structured and supports SEO goals.
           - Coordinate with the **project manager** to align the sitemap with timelines, resources, and budgets.

        4. **Provide Deliverables and Documentation:**
           - Create a **sitemap document** (visual or diagrammatic) showing the website's structure.
           - Develop a **requirements document** outlining the functional requirements for each page or feature.
           - Ensure **stakeholder sign-off** on the sitemap before moving to design and development phases.
           - Document **user stories** or **use cases** that align with the sitemap.
           - If necessary, provide a **content strategy plan** for structuring and delivering content on the website.

        Ensure that all documentation is clear, accurate, and facilitates the smooth transition to the design phase of the project.
        Generate sitemap, refer this {PageExamples} json examples. if navbar and footer description is empty generate possible description.
        always stick with same response format that is mentioned below and always return the users business_name and business_description from thier input.
        **Example Output JSON:**
            {output_json}
           
        """

        response = get_llm_response(
            user_prompt=f"Generate a sitemap for the given {data.business_name}, {data.business_description}, {data.sitemap_prompt}. make sure to generate number of pages based on the user's given {data.page} requirement",
            system_prompt=prompt
        )
        json_res = json.loads(response)


        hero_prompt = f"Generate a high-quality hero section image for a website representing the business '{data.business_description}. only generate the image Dont generate anyother contents.'."

        try:
            hero_image = self.generate_image(hero_prompt)
            hero_image_url = self.save_base_64(

                hero_image,
                folder="src/images",
                image_format="png",
                filename="hero_image"

            )
            json_res["imageUrl"] = hero_image_url
        except Exception as e :
            json_res["imageUrl"] = None
        return json_res


