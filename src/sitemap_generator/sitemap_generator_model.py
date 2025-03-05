from pydantic import BaseModel, Field
from typing import Optional


class SitemapGenerator(BaseModel):
    sitemap_prompt: str = Field(..., alias="prompt")
    page: Optional[int] = None
    language: Optional[str] = None

