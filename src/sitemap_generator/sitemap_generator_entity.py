from src.config import config
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class SitemapGenerator(config.Base):
    __tablename__ = "sitemap_generator"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)

