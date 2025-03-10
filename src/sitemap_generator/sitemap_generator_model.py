from pydantic import BaseModel, Field
from typing import Optional


class SitemapGenerator(BaseModel):
    business_name: str = Field(..., alias = "businessName")
    business_description: str = Field(...,alias = "businessDescription")
    sitemap_prompt: str = Field(..., alias="prompt")
    page: Optional[int] = None
    language: Optional[str] = None

