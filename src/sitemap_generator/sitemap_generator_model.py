from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from enum import Enum


class SitemapGenerator(BaseModel):
    business_name: str = Field(..., alias="businessName")
    business_description: str = Field(..., alias="businessDescription")
    sitemap_prompt: Optional[str] = Field(..., alias="prompt")
    page: Optional[int] = None
    language: Optional[str] = None

class FontStyle(BaseModel):
    description: str

class CSSProperties(BaseModel):
    font_family: str
    font_size: str
    font_weight: Optional[str] = None

class CSSExample(BaseModel):
    selector: str
    properties: CSSProperties

class FontExample(BaseModel):
    css: CSSExample

class BrandLogoFont(BaseModel):
    name: str
    logo_name: str
    style: FontStyle
    best_for: str
    link: str
    example: FontExample

BrandLogofontSchema = List[BrandLogoFont]

class FontWeight(int, Enum):
    Thin = 100
    ExtraLight = 200
    Light = 300
    Regular = 400
    Medium = 500
    SemiBold = 600
    Bold = 700
    ExtraBold = 800
    Black = 900

class ScaleEnum(str, Enum):
    MINOR_SECOND = "1.067"
    MAJOR_SECOND = "1.125"
    MINOR_THIRD = "1.200"
    MAJOR_THIRD = "1.250"
    PERFECT_FOURTH = "1.333"
    AUGMENTED_FOURTH = "1.414"
    PERFECT_FIFTH = "1.500"
    GOLDEN_RATIO = "1.618"
    CUSTOM = "custom"

class Font(BaseModel):
    font_family:str
    base_fontsize:int
    font_weight:List[FontWeight]
    line_height:int
    typescale_ratio:ScaleEnum


class BrandColor(BaseModel):
    primary_color: str
    secondary_color: str

class ColorPalette(int, Enum):
    Monochromatic = 1
    Analogous = 2
    Complementary = 3
    Triadic = 4
    Tetradic = 5



class BrandColorSchema(BaseModel):
    colors: BrandColor
    ColorPalette: ColorPalette
    ColorPalette_description: str



class VisualBrandGuidelines(BaseModel):
    Logo_typeface: BrandLogofontSchema
    font: Font
    colors: BrandColorSchema



class ProjectBrief(BaseModel):
    business_name: str
    business_description: str
    website_goal: str
    target_audience: str
    VisualBrandGuidelines: VisualBrandGuidelines
    pageCount: Optional[int] = None
    language: Optional[str] = None


class SectionName(str, Enum):
    Navbar = "Navbar"
    Hero_Header_Section = "Hero Header Section"
    Header_Section = "Header Section"
    Portfolio_Item_Header_Section = "Portfolio Item Header Section"
    Project_Item_Header_Section = "Project Item Header Section"
    Portfolio_Item_Body_Section = "Portfolio Item Body Section"
    Project_Item_Body_Section = "Project Item Body Section"
    Portfolio_List_Section = "Portfolio List Section"
    Project_List_Section = "Project List Section"
    Blog_Post_Header_Section = "Blog Post Header Section"
    Resource_Item_Header_Section = "Resource Item Header Section"
    Case_Study_Header_Section = "Case Study Header Section"
    Press_Article_Header_Section = "Press Article Header Section"
    Update_Item_Header_Section = "Update Item Header Section"
    Event_Item_Header_Section = "Event Item Header Section"
    Blog_Post_Body_Section = "Blog Post Body Section"
    Resource_Item_Body_Section = "Resource Item Body Section"
    Case_Study_Body_Section = "Case Study Body Section"
    Documentation_Body_Section = "Documentation Body Section"
    Press_Release_Body_Section = "Press Release Body Section"
    Legal_Page_Body_Section = "Legal Page Body Section"
    Update_Item_Body_Section = "Update Item Body Section"
    Event_Schedule_Section = "Event Schedule Section"
    Event_Item_Body_Section = "Event Item Body Section"
    Course_Item_Body_Section = "Course Item Body Section"
    Featured_Blog_List_Header_Section = "Featured Blog List Header Section"
    Featured_Resources_List_Header_Section = "Featured Resources List Header Section"
    Featured_Case_Study_List_Header_Section = "Featured Case Study List Header Section"
    Featured_Press_List_Header_Section = "Featured Press List Header Section"
    Featured_Updates_List_Header_Section = "Featured Updates List Header Section"
    Featured_Events_List_Header_Section = "Featured Events List Header Section"
    Featured_Courses_List_Header_Section = "Featured Courses List Header Section"
    Blog_List_Section = "Blog List Section"
    Resources_List_Section = "Resources List Section"
    Case_Study_List_Section = "Case Study List Section"
    Press_List_Section = "Press List Section"
    Updates_List_Section = "Updates List Section"
    Events_List_Section = "Events List Section"
    Courses_List_Section = "Courses List Section"
    Feature_Section = "Feature Section"
    Features_List_Section = "Features List Section"
    Benefits_Section = "Benefits Section"
    How_It_Works_Section = "How It Works Section"
    Services_Section = "Services Section"
    About_Section = "About Section"
    Stats_Section = "Stats Section"
    Ecommerce_Product_Section = "Ecommerce Product Section"
    Timeline_Section = "Timeline Section"
    Ecommerce_Product_Header_Section = "Ecommerce Product Header Section"
    Course_Item_Header_Section = "Course Item Header Section"
    Ecommerce_Products_List_Section = "Ecommerce Products List Section"
    Testimonial_Section = "Testimonial Section"
    Reviews_Section = "Reviews Section"
    Pricing_Section = "Pricing Section"
    Pricing_Comparison_Section = "Pricing Comparison Section"
    CTA_Section = "CTA Section"
    CTA_Form_Section = "CTA Form Section"
    Newsletter_Section = "Newsletter Section"
    Early_Access_Section = "Early Access Section"
    Contact_Section = "Contact Section"
    Contact_Form_Section = "Contact Form Section"
    Application_Form_Section = "Application Form Section"
    Locations_Section = "Locations Section"
    Gallery_Section = "Gallery Section"
    FAQ_Section = "FAQ Section"
    Team_Section = "Team Section"
    Logo_List_Section = "Logo List Section"
    Award_Logos_List_Section = "Award Logos List Section"
    Customer_Logos_List_Section = "Customer Logos List Section"
    Client_Logos_List_Section = "Client Logos List Section"
    Partner_Logos_List_Section = "Partner Logos List Section"
    Job_Listings_Section = "Job Listings Section"
    Footer = "Footer"
    Comparison_Section = "Comparison Section"





# {
#     section:{
#         Layout:{
#             Grid:"Grid",
#             Flexbox:"Flexbox",
#         }
#         UiElements:
#             [{
#                 ui_element_type:[UIElementType],
#                 alignment:[alignment],
#                 spacing:[spacing]
#             },
#             {
#                 ui_element_type:[UIElementType],
#                 alignment:[alignment],
#                 spacing:[spacing]
#             }
#             ],        
#     }
# }







class SectionOutline(BaseModel):
    section_name: SectionName = Field(
        description="Use only the section names to name the section"
    )
    section_instruction: str = Field(
        description=" Instruction to describe what the section should contian keep the sentence short"
    )
    section_description:str = Field(description="Description about the section and its children in a sentence")
   


class Page(BaseModel):
    page_id: int
    Pagename: str
    sections: list[SectionOutline]


class Pages(BaseModel):
    websitename: str
    Numberofpages: int
    pages: list[Page]
