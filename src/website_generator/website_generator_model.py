from pydantic import BaseModel, Field
from typing import  Any





class Sitemap(BaseModel):
    projectBrief: Any
    pageTitle: str = Field(...)
    sections: Any



class Website(BaseModel):
    code: str = Field(..., description="The generated website code")
    








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
