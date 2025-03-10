from .website_generator_model import Sitemap
from .website_generator_entity import WebsiteGenerator as WebsiteGeneratorEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable
from src.utils.llm_call import get_llm_response
import json

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

@Injectable
class WebsiteGeneratorService:

    @async_db_request_handler
    async def add_website_generator(self, website_generator: Sitemap, session: AsyncSession):
        new_website_generator = WebsiteGeneratorEntity(
            **website_generator.dict()
        )
        session.add(new_website_generator)
        await session.commit()
        return new_website_generator.id

    @async_db_request_handler
    async def get_website_generator(self, session: AsyncSession):
        query = select(WebsiteGeneratorEntity)
        result = await session.execute(query)
        return result.scalars().all()
    
    async def generate_website(self, data: Sitemap):
        prompt = """
        You are an expert content optimizer specializing in concise descriptions for website sections. Your task is to analyze a JSON object representing a website's structure, specifically the `sections` array within each page, and rewrite the `sectionDescription` to be a concise, action-oriented statement of purpose. Maintain the same JSON structure.

        **Characteristics of Excellent Statements of Purpose (for sectionDescription):**

        * **Action-Oriented:** Start with a strong verb indicating the section's intended outcome.
        * **Concise:** Use as few words as possible to convey the core message.
        * **Clear and Unambiguous:** Easily understood.
        * **Specific:** Focus on the purpose of that section.
        * **User-Centric:** Consider the user's perspective.

        **Example Input JSON:**

        ```json
        {
            "pageTitle": "Homepage",
            "sections": [
                {
                    "sectionTitle": "Hero Section",
                    "sectionDescription": "This section introduces the product with a captivating headline and visuals."
                },
                {
                    "sectionTitle": "Features Section",
                    "sectionDescription": "This section highlights the key features of the product and their benefits."
                }
            ]
        }
        ```

        **Example Output JSON (with tweaked sectionDescription):**
        {
            "pageTitle": "Homepage",
            "sections": [
                {
                    "sectionTitle": "Hero Section",
                    "sectionDescription": "Introduce the product with captivating visuals and headlines."
                },
                {
                    "sectionTitle": "Features Section",
                    "sectionDescription": "Highlight key product features and their benefits."
                }
            ]
        }
        """
        response = get_llm_response(
            user_prompt=f"Please process the following JSON according to the instructions in the system prompt:{data.sections}",
            system_prompt=prompt
        )
        json_res = json.loads(response)

        web_res = get_llm_response(
            user_prompt= f"""Create a fully styled and animated homepage for {data.businessName}, {data.businessDescription}, {response}""",
                system_prompt = '''

                                    Your a AI developer who can Create a fully styled and animated homepage. 
                    you know how to craft them using grids to create stunning website layouts

                    using Webflow-compatible components.
                    The page should include:
                    A responsive layout following best UI/UX practices.
                    A fixed navigation bar with smooth scrolling.
                    A hero section with a call-to-action (CTA) and an animated headline.
                    A logo section showing trusted companies, animated on load.
                    A benefits section listing key product advantages.
                    A how-it-works section explaining functionality visually.
                    Feature sections describing core product capabilities.
                    Testimonial sections with animated user feedback.
                    A FAQ section using an accordion format.
                    A footer with navigation and contact details.

                    Technical Requirements:
                    Fully responsive (desktop, tablet, mobile).
                    CSS animations (e.g., fade-ins, slide-ups, hover effects).
                    Smooth transitions for interactive elements.
                    Semantic HTML and minimal JavaScript (if needed).
                    Use Webflow-compatible structure for easy import.
                    Generate a single HTML file containing all the <html><styles> and <scripts>:
                    The complete HTML structure.
                    CSS for styling and animations.
                    Any JavaScript needed for interactions.
                    🎯 Goal: The page should feel modern, interactive, and engaging for [Tech-savvy fashion enthusiasts
                    Eco-conscious consumers
                    Trendsetters and influencers



                    Choose a copywriting Framework that suites the business
                    4Ps: Picture, Promise, Proof, Push
                    AIDA: Attention, Interest, Desire, Action
                    APP: Awareness, Problem, Positioning
                    Before-After-Bridge: Before state, After state, Bridge to achieve the After state
                    FAB: Features, Advantages, Benefits
                    Great Leads: Direct, Indirect, News, How-to, Question, Command, Testimonial, Story, Quotation
                    PAPA: Problem, Agitate, Persuade, Asks
                    PAS: Problem, Agitation, Solution
                    StoryBrand: Character, Problem, Guide, Plan, Call to Action
                    The 5 Cs: Clear, Concise, Compelling, Credible, Customer-focused

                    For each section create website copy using the framework

                    Pick the appropriate webflow component layouts
                    -Use Image placeholders wherever required. For Placeholder image use this URL with the imagebackground and makesure to replace the image width and height in the end of the URL
                     https://placehold.co/WxH  //Replace width of the image and height of the image in number
                    -Modern, sleek and eye pleasing
                    - For User avatar use this link https://avatar.iran.liara.run/public
                    dont response anyother than code.
                    Make sure response in json format.

                    {
                        code: your generated code here.....
                    }
                        '''
        )
        
        json_web = json.loads(web_res)
         
        
        return json_web
