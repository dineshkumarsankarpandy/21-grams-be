from src.config import config
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class WebsiteImage(config.Base):
    __tablename__ = "website_image"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)

