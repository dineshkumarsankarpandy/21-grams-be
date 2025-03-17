from .website_image_model import WebsiteImage
from .website_image_entity import WebsiteImage as WebsiteImageEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable
import google.generativeai as genai
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import base64
from google.genai import types  # Corrected import
import magic
import re
import json
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@Injectable
class WebsiteImageService:
    @async_db_request_handler
    async def add_website_image(self, website_image: WebsiteImage, session: AsyncSession):
        new_website_image = WebsiteImageEntity(**website_image.dict())
        session.add(new_website_image)
        await session.commit()
        return new_website_image.id

    @async_db_request_handler
    async def get_website_image(self, session: AsyncSession):
        query = select(WebsiteImageEntity)
        result = await session.execute(query)
        return result.scalars().all()

    async def generate_website_img(self, data: WebsiteImage):
        base64_str:str
        if data.image.startswith("data:"):
            match = re.search(r'^data:[\w/]+;base64,(.+)$', data.image)
            if not match:
                raise ValueError("Invalid base64 image data.")
            base64_str = match.group(1)
        else:
            base64_str = data.image

        base64_str = base64_str.strip()
        padding = len(base64_str) % 4
        if padding:
            base64_str += "=" * (4 - padding)
     
        text_prompt = (
            "Based on this image, generate a complete HTML file with embedded CSS and JavaScript "
            "to create a website that matches the image. Provide the entire code as a single string. "
            "Make sure to stick with this output format: "
            "Only the code should be in the string. Avoid any other text."
        )

        response = model.generate_content([

            text_prompt,
            {"inline_data": {"mime_type": "image/png", "data": base64_str}}
        ]
            
        )
        generated_code = response.text.strip()
        if generated_code.startswith("```html"):
            generated_code = generated_code[7:]
        if generated_code.endswith("```"):
            generated_code = generated_code[:-3]
    
        return generated_code