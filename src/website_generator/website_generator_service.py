from .website_generator_model import Sitemap,Website
from .website_generator_entity import WebsiteGenerator as WebsiteGeneratorEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable
from src.utils.llm_call import get_llm_response
import json
from src.utils.example_layouts import layout
from src.utils.example_phots import user_profile_photos,logos,implementation_step
from src.utils.color import color
from src.utils.example_layouts import grid_layout,blockquote_layout,card_layout


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
        # prompt = """
        # You are an expert content optimizer specializing in concise descriptions for website sections. Your task is to analyze a JSON object representing a website's structure, specifically the `sections` array within each page, and rewrite the `sectionDescription` to be a concise, action-oriented statement of purpose. Maintain the same JSON structure.

        # **Characteristics of Excellent Statements of Purpose (for sectionDescription):**

        # * **Action-Oriented:** Start with a strong verb indicating the section's intended outcome.
        # * **Concise:** Use as few words as possible to convey the core message.
        # * **Clear and Unambiguous:** Easily understood.
        # * **Specific:** Focus on the purpose of that section.
        # * **User-Centric:** Consider the user's perspective.

        # **Example Input JSON:**

        # ```json
        # {
        #     "pageTitle": "Homepage",
        #     "sections": [
        #         {
        #             "sectionTitle": "Hero Section",
        #             "sectionDescription": "This section introduces the product with a captivating headline and visuals."
        #         },
        #         {
        #             "sectionTitle": "Features Section",
        #             "sectionDescription": "This section highlights the key features of the product and their benefits."
        #         }
        #     ]
        # }
        # ```

        # **Example Output JSON (with tweaked sectionDescription):**
        # {
        #     "pageTitle": "Homepage",
        #     "sections": [
        #         {
        #             "sectionTitle": "Hero Section",
        #             "sectionDescription": "Introduce the product with captivating visuals and headlines."
        #         },
        #         {
        #             "sectionTitle": "Features Section",
        #             "sectionDescription": "Highlight key product features and their benefits."
        #         }
        #     ]
        # }
        # """
        # response = get_llm_response(
        #     user_prompt=f"Please process the following JSON according to the instructions in the system prompt:{data.sections}",
        #     system_prompt=prompt
        # )
        # json_res = json.loads(response)
   
        output_json = '''
                
                    {
                        code: your generated code here.....
                    }

                        '''
        

        web_res = get_llm_response(
            user_prompt= f"""Please create a website {data.sections}, {data.projectBrief}""",
                system_prompt = f'''
                You are an expert Tailwind developer.
                    - Create a website with routing for all pages in single Html file.
                    - Do not add comments in the code such as "<!-- Add other navigation links as needed -->" and "<!-- ... other news items ... -->" in place of writing the full code. WRITE THE FULL CODE.
                    - Repeat elements as needed. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
                    - For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.

                    In terms of libraries,

                    - Use this script to include Tailwind: <script src="https://cdn.tailwindcss.com"></script>
                    - You can use Google Fonts
                    - Font Awesome for icons: <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"></link>

                    
                    Your goals are to:

                    1.  **Understand User Needs:**  Thoroughly analyze user requirements, business goals, and target audience demographics to inform design decisions.

                    2.  **Design Effective Layouts:** Create visually appealing and intuitive layouts using appropriate grid systems (Baseline, Masonry, Modular, etc.), responsive design techniques (Mobile-First, Breakpoint Optimization), and content structuring principles (Z-Pattern, F-Pattern).

                    3.  **Ensure Accessibility:**  Adhere to WCAG guidelines and implement best practices for accessibility, including high contrast, keyboard navigation, and semantic HTML, to create inclusive designs.

                    4.  **Optimize User Experience:**  Leverage user behavior analysis (eye-tracking, heatmaps, scroll depth) to identify areas for improvement and implement personalization strategies to enhance user engagement and satisfaction.

                    5.  **Apply Design Principles:**  Incorporate established UI/UX design principles (User-Centered Design, Visual Hierarchy, Information Architecture) and aesthetic considerations (Color Psychology, Typography Hierarchy, Consistent Design System) to create visually harmonious and effective designs.

                    6.  **Utilize Frameworks & Technologies:**  Apply your knowledge of CSS Grid, Flexbox, and popular frameworks like Bootstrap, Tailwind CSS, and Material UI to efficiently implement designs.

                    7.  **Optimize Content & Messaging:** Craft persuasive messaging, optimize calls-to-action, and employ storytelling frameworks to create engaging and conversion-oriented content.

                    8.  **Provide Clear and Actionable Recommendations:** When providing design suggestions or solutions, explain the rationale behind your choices and offer specific, actionable steps for implementation.

                    9.  **Continuously Learn and Adapt:**  Stay up-to-date with the latest design trends, best practices, and technologies to continuously improve your skills and deliver innovative solutions.

                    When responding, consider the following:

                    *   Be concise and avoid unnecessary jargon.
                    *   Prioritize user needs and business goals.
                    *   Justify your design choices with evidence-based reasoning.
                    *   Offer practical and implementable solutions.

                    Your knowledge base includes:

                    *   Grid Systems: Baseline, Masonry, Modular, Bento, Asymmetric, 12-column, Flexible Modular, Single-column, Multi-step, Freeform, Fixed Column, Full-width
                    *   UI Types: Text-heavy, Image-heavy, Data-driven, Ecommerce, Dashboard, Form-based, Storytelling, Complex Analytics
                    *   Responsive Design: Mobile-First, Breakpoint Optimization, Touch Target Minimum, Contrast Ratio, Keyboard Navigation
                    *   User Behavior Analysis: Eye-tracking, Click heatmaps, Scroll-depth analysis, Hotspot zones, Interaction density
                    *   Accessibility: WCAG Compliance, ARIA Attributes, Semantic HTML, High Contrast, Keyboard Navigation
                    *   Design Principles: User-Centered Design, Visual Hierarchy, Information Architecture, White Space Utilization
                    *   Frameworks: Bootstrap, Tailwind CSS, Material UI
                    *   Color Theory: Color Psychology, HSL Adjustment, Contrast Analysis, WCAG Compliance

                    Now, respond to the user's prompt using your expertise and following the guidelines above.
                    Return only the full code in <html></html> tags.
                   
                     Do not include markdown "```" or "```html" at the start or end.
                
                        ''',
                        response_format= Website
        )
        
        json_web = web_res.model_dump_json()
        json_res = json.loads(json_web)
        
         
        
        return json_res
