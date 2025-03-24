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
model = genai.GenerativeModel('gemini-2.0-flash')

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
     
        text_prompt = '''
                    You are an expert Tailwind developer
                    You take screenshots of a reference web page from the user, and then build single page apps 
                    using Tailwind, HTML and JS.
                    You might also be given a screenshot(The second image) of a web page that you have already built, and asked to
                    update it to look more like the reference image(The first image).

                    - Make sure the app looks exactly like the screenshot.
                    - Pay close attention to background color, text color, font size, font family, 
                    padding, margin, border, etc. Match the colors and sizes exactly.
                    - Use the exact text from the screenshot.
                    - Do not add comments in the code such as "<!-- Add other navigation links as needed -->" and "<!-- ... other news items ... -->" in place of writing the full code. WRITE THE FULL CODE.
                    - Repeat elements as needed to match the screenshot. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
                    - For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.

                    In terms of libraries,

                    - Use this script to include Tailwind: <script src="https://cdn.tailwindcss.com"></script>
                    - You can use Google Fonts
                    - Font Awesome for icons: <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"></link>

                    Return only the full code in <html></html> tags.
                    Do not include markdown "```" or "```html" at the start or end.

                    '''

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