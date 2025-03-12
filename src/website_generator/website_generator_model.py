from pydantic import BaseModel, Field
from typing import List, Dict,Optional


class Section(BaseModel):
    sectionTitle: str = Field(...)
    sectionDescription: str = Field(...)


class Sitemap(BaseModel):
    businessName: str = Field(...)
    businessDescription: str = Field(...)
    imageUrl:Optional[str] = Field(...)
    pageTitle: str = Field(...)
    sections: List[Section] = Field(...)




    








#     {
#     "pageTitle": "Homepage",
#     "sections": [
#         {
#             "sectionTitle": "Hero Banner",
#             "sectionDescription": "Introduction section with a striking visual of Dinesh Kumar and a tagline that emphasizes his professional skills as a web developer. Features a strong call-to-action leading to the portfolio section."
#         },
#         {
#             "sectionTitle": "Tech Stack Highlights",
#             "sectionDescription": "Summary of the key technologies and frameworks Dinesh specializes in, using iconography and brief descriptions to capture user attention."
#         },
#         {
#             "sectionTitle": "Navigation Summary",
#             "sectionDescription": "Quick access links to critical sections such as About, Portfolio, Blog, and Contact to ensure optimal user flow."
#         }
#     ]
# }
