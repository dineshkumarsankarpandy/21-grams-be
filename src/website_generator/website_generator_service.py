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
        
        project_brief = '''
                {
                "business_name":"Plan Z",
                "business_description":"Plan Z is a creative agency that specializes in innovative UI/UX design, branding, and digital experiences. With a blend of storytelling, aesthetics, and functionality, we craft visually compelling and user-friendly designs. 
                Our expertise extends to website and app design, product branding, and strategic design consulting, ensuring that every project resonates with its target audience while strengthening brand identity.",
                "website_goal":"Develop a dynamic and engaging digital presence that effectively showcases our creative portfolio, highlights our design expertise, and attracts a diverse range of clients seeking exceptional digital solutions.",
                "target_audience":"Businesses of all sizes, startups, and established organizations in need of innovative design solutions to enhance their brand identity and user experience."
                }
            '''


        web_res = get_llm_response(
            user_prompt= f"""please create me a landing page using grids make it creative designed extremely well.
              create all components required {data.sections},{project_brief}""",
                system_prompt = f'''
                As a specialized AI agent in crafting beautiful websites with considering responsiveness understanding the requirement domain and the given user requirement with the Instructions you have, complete it.
                                        
                    <Rules>
                    - Create a checklist to compare designs against benchmarks systematically.
                    - Create a designsystem with tokens to maintain consistent.
                    - Understand and come up with a sitemap for one page of the website
                    - Think of a perfect idea how to present them creatively
                    - Leave using traditional grid system use different grid to come up with new design layouts
                    - Respect the golden ratio.Make Room for White Space
                    - Use the Rule of Thirds in order to determine some of the most important grid and layout-related design decisions, such as: 
                    - What type of grid to use
                    - What dimensions each grid element should have
                    - Where to place the most important elements
                    - What your image ratios should be
                    - How much negative space to add around and between elements
                                
                    1. Hierarchical Grids
                    What It Is: A hierarchical grid prioritizes certain elements over others, creating a clear visual hierarchy to guide the user’s attention.
                    When to Use: Ideal for content-heavy sections where you need to emphasize key information.
                    Examples:
                    Blogs: A blog layout with a large featured article at the top (e.g., a prominent headline and image), followed by smaller grids for related posts or a sidebar with ads.
                    News Websites: A news homepage with a full-width banner for breaking news, a two-column grid for secondary stories, and a sidebar for trending topics.
                    Why It Works: It helps users quickly find the most important content, enhancing readability and engagement.

                    2. Modular Grids
                    What It Is: A modular grid divides the layout into equal-sized modules, creating a symmetrical and balanced design.
                    When to Use: Perfect for layouts where items need equal emphasis and consistency.
                    Examples:
                    Product Galleries: An e-commerce site with a 3x3 grid of product cards (e.g., each showing an image, title, and price) for easy comparison.
                    Portfolios: A photographer’s portfolio with a grid of uniform thumbnails, each linking to a project page, for a clean and organized look.
                    Why It Works: It provides a structured, professional layout that’s easy to scan and visually harmonious.

                    3. Asymmetrical Grids
                    What It Is: An asymmetrical grid avoids strict symmetry, using varied sizes and shapes for a dynamic, modern feel.
                    When to Use: Great for designs that aim to stand out or create visual interest.
                    Examples:
                    Creative Agency Websites: A homepage with overlapping images, varied text blocks, and unconventional spacing to reflect a unique brand identity.
                    Landing Pages: A product landing page with a large hero image on one side and staggered content blocks on the other, directing focus to a call-to-action (CTA).
                    Why It Works: It adds movement and freshness, making the design feel engaging and contemporary.

                    #Testing Grid Layouts for Responsiveness
                    To ensure your grid works well across devices (e.g., desktop, tablet, mobile), follow these steps:

                    Use CSS Tools: Implement grids with CSS Grid or Flexbox for flexibility. For example, a 3-column modular grid on desktop can stack into a single column on mobile using media queries.
                    Check Breakpoints: Test at common screen sizes (e.g., 320px for mobile, 768px for tablet, 1024px for desktop) to confirm content reflows smoothly.
                    Ensure Accessibility: Verify that key content stays visible and navigation remains intuitive on smaller screens.
                    Simulate Devices: Use browser developer tools to preview how the grid adapts to different devices.
                    Why It Matters: Responsive grids guarantee a seamless user experience, keeping your site functional and attractive no matter the screen size.
                                
                    <Grid-layout>
                            strictly follow this {grid_layout} for grid layout.
                    </Grid-layout>

                    
                    ##2. Blockquote Section
                    Blockquote sections are used to highlight important quotes or testimonials on a website. They help break up the content and draw attention to key messages. Here’s how to create effective blockquote sections:
                    <blockquote-ideas>
                        {blockquote_layout}
                    </blockquote-ideas>

                    ##3. cards for blog section

                    ##4. Colors and Fonts
                    Creating a visually appealing and functional website requires careful selection of colors and fonts. This section outlines how to choose Pantone colors, pair fonts effectively, and meet WCAG accessibility standards for color contrast, with actionable steps and examples.

                    1. Choosing Pantone Colors
                    Pantone colors are standardized shades that ensure consistency across digital and print designs. To select the right ones for your website:

                    Use Tools: Leverage Adobe Color or Coolors to explore and pick Pantone colors that reflect your brand’s identity.
                    Align with Brand: Choose colors that match your brand’s vibe—bold shades for energy (e.g., "Living Coral") or muted tones for sophistication (e.g., "Khaki").
                    Examples:
                    A tech startup might use "Classic Blue" for trust and reliability.
                    An eco-friendly brand could pick "Greenery" for a natural, sustainable feel.
                    Result: These choices create an emotional connection with users and keep your branding consistent.

                    2. Pairing Fonts
                    Font pairing combines different typefaces to balance contrast and harmony, improving both readability and style.

                    How to Pair: Combine a serif font (decorative, traditional) for headings with a sans-serif font (clean, modern) for body text.
                    Tool Tip: Use Google Fonts to find free, web-friendly options.
                 
                    3. Meeting WCAG Accessibility Standards for Color Contrast
                    The Web Content Accessibility Guidelines (WCAG) ensure your site is readable for everyone, including those with visual impairments, by requiring sufficient color contrast.

                    Standards: Aim for a 4.5:1 contrast ratio for normal text and 3:1 for large text (like headings).
                    Examples:
                    High Contrast: Black text (#000000) on a white background (#FFFFFF) offers a 21:1 ratio—perfectly accessible.
                    Low Contrast: Light gray text (#CCCCCC) on white (#FFFFFF) yields a 1.6:1 ratio—too faint to meet standards.
                    Tool Tip: Check your combinations with WebAIM’s Contrast Checker.
                    Result: Adhering to these ratios makes your site inclusive and user-friendly, while also boosting accessibility and SEO.
                    
                    - Import suitable google fonts for the brand
                    - Choose a color palette that aligns with the brand identity
                    - Generate Section copy based on frameworks
                    - More importance on the Home page - the value proposition of the platform is given so much emphasis and “time to shine” on the homepage, it’s crystal clear to website visitors what the added value is that they’re about to encounter.
                    - For Each section Think of the best  15 ways you can represent them and pick one among each sections
                    - Each section would have evolved a lot understand them and implement it
                                
                 
                                - for image placeholders use this  input the necessary value <img src= https://placehold.co/widthxheight/bgColor/textColor'' alt="Placeholder image" style= width, height  />
                                -for testimonials, team members, our team, founders, individual members use these {user_profile_photos}    
                                </Rules>

                    <ImportantRules>
                        Create a sitemap with user journey mapping and accessibility features.
                        Use the golden ratio (1:1.618) and rule of thirds for layouts, emphasizing visual hierarchy.
                        Select grids based on content: hierarchical for complexity, modular for symmetry, asymmetrical for modernity.
                        Choose Pantone colors with harmony tools and pair fonts for readability.
                        Generate section copy with frameworks like PAS, weaving in brand storytelling.
                        Design responsive navbars (sticky or scroll-triggered) and interactive footers (20svh–70svh).
                        Use accordions and cards with micro-interactions, balancing UX and content width.
                        Prioritize mobile-first hero sections, evaluated with a checklist.
                        Apply a spacing scale and optimize performance with compressed images and lazy loading.
                    </ImportantRules>

                    <Instructions>

                    1. Technical Implementation
                    Import only necessary Tailwind classes (e.g., flex, grid, text-) to keep code lean.
                    Optimize CDN links by minifying or combining them for faster load times.
                    Provide a Tailwind setup guide with comments for maintainability.

                    2. Benchmarking
                    Compare elements (e.g., scroll animations, typography) to Webflow and Awwwards designs.
                    Review trends quarterly to stay current.
                    Use a checklist to systematically evaluate your designs against benchmarks.


                    SEO: Use semantic HTML, alt text, and meta tags for better search visibility.
                    Accessibility: Ensure WCAG 2.1 compliance (e.g., color contrast, ARIA labels).
                    Content Management: Plan for a headless CMS (e.g., Contentful) for easy updates.
                    Version Control: Use Git for tracking changes and collaboration.
                    Design System: Create a style guide (e.g., colors, typography, components) for consistency.
                    Analytics: Add tools like Google Analytics to monitor user behavior.
                    Security: Use HTTPS and sanitize inputs to protect data

                    </Instructions>

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
                    Eco-conscious consumers
                    Trendsetters and influencers
                    

                    <Photo-library>
                    use this cdn links from the example for square photos.{user_profile_photos}
                    for example you can use this in testimonials, team members, wherever you want to represent a person.
                    </Photo-library>

                    <logos>
                        Use the provided object alter them if needed to dynamically render company logos in a grid layout. use gsap and come up with a seamless way to infinite scroll through the logos.
                        {logos}. follow this for light theme.{implementation_step}. add infinite autoscroll animation for logos.

                    </logos>

                    ##3. cards 
                     use these cards for section {card_layout}
                    <card-layout>
                        {card_layout}
                    </card-layout>

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

                    For each section create website copy using the framework make sure it should not add the keywords like 4ps, AIDA, APP, Before-After-Bridge, FAB, Great Leads, PAPA, PAS, StoryBrand, The 5 Cs.It should only contain the content.

                    Pick the appropriate webflow component layout.

                    dont response anyother than code.
                   

                        ''',
                        response_format= Website
        )
        
        json_web = web_res.model_dump_json()
        json_res = json.loads(json_web)
        
         
        
        return json_res
