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
        new_sitemap_generator = SitemapGeneratorEntity(**sitemap_generator.dict())
        session.add(new_sitemap_generator)
        await session.commit()
        return new_sitemap_generator.id

    @async_db_request_handler
    async def get_sitemap_generator(self, session: AsyncSession):
        query = select(SitemapGeneratorEntity)
        result = await session.execute(query)
        return result.scalars().all()

    async def generate_sitemap_generator(self, data: SitemapGenerator):
        prompt = """
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

        Ensure that all documentation is clear, accurate, and facilitates the smooth transition to the design phase of the projec
        always stick with same response format that is mentioned below and always return the users business_name and business_description from thier input.
        **Example Output JSON:**
        {
        "businessName:" "users business name here...",
        "businessDescription:" "users description here..."
        "pages":[
        "pageTitle": "Home",//always generate first has Home.
        "sections": [
            {
            "sectionTitle": "section title here.......",
            "sectionDescription": "sections Description here...."
            }
        
        ]

        ]
        }
        """
 
        response = get_llm_response(
            user_prompt=f"Generate a sitemap for the given {data.business_name}, {data.business_description} {data.sitemap_prompt} ...",
            system_prompt=prompt
        )
        json_res = json.loads(response)
        return json_res


