from .sitemap_generator_model import SitemapGenerator
from .sitemap_generator_entity import SitemapGenerator as SitemapGeneratorEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable
import openai
import os
import json

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.llm_call import get_llm_response

openai.api_key = os.environ.get("OPENAI_API_KEY")


@Injectable
class SitemapGeneratorService:

    @async_db_request_handler
    async def add_sitemap_generator(self, sitemap_generator: SitemapGenerator, session: AsyncSession):
        new_sitemap_generator = SitemapGeneratorEntity(
            **sitemap_generator.dict()
        )
        session.add(new_sitemap_generator)
        await session.commit()
        return new_sitemap_generator.id

    @async_db_request_handler
    async def get_sitemap_generator(self, session: AsyncSession):
        query = select(SitemapGeneratorEntity)
        result = await session.execute(query)
        return result.scalars().all()

    async def generate_sitemap_generator(self, data: SitemapGenerator):
        prompt = '''
            "Based on the user's website requirements, First of all you only need to generate for Home page.you need to generate sections that is need to be in this page and that sections description, generate a JSON object with the following structure:

                    json
                    {
                    \"page_section\": \"[Relevant section of the page]\",
                    \"page_description\": \"[Brief description of the page]\"
                    }

                '''
        response = get_llm_response(user_prompt=data.sitemap_prompt, system_prompt=prompt)
        json_res = json.loads(response)
        return json_res
