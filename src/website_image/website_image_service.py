from .website_image_model import WebsiteImage
from .website_image_entity import WebsiteImage as WebsiteImageEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable
import google.generativeai as genai
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import base64
from google.genai import types
import magic
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')


@Injectable
class WebsiteImageService:

    @async_db_request_handler
    async def add_website_image(self, website_image: WebsiteImage, session: AsyncSession):
        new_website_image = WebsiteImageEntity(
            **website_image.dict()
        )
        session.add(new_website_image)
        await session.commit()
        return new_website_image.id

    @async_db_request_handler
    async def get_website_image(self, session: AsyncSession):
        query = select(WebsiteImageEntity)
        result = await session.execute(query)
        return result.scalars().all()
    

    async def generate_website_img(self, data: WebsiteImage):
        # Decode the base64 image
        image_bytes = base64.b64decode(data.image)
        # mime_type = magic.from_buffer(image_bytes, mime=True)

        # if not mime_type:
        #     return 'Error: Unable to determine the type of the image.'
        image_part = types.Part(
            data= types.Blob(
                mime_type= "image/png",
                # data= data.base64_image
                data=image_bytes
            )
        )
     

        # Specific prompt for the desired output
        text_prompt = (
            "Based on this image, generate a complete HTML file with embedded CSS and JavaScript "
            "to create a website that matches the image. Provide the entire code as a single string."
        )

        text_part = types.Part(text=text_prompt)


        # Generate content using the model
        response = model.generate_content(
            contents=[text_part,image_part]
        )
        generated_code = response.text  # Extract the generated text
        return generated_code
    
