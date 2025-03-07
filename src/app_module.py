from nest.core import PyNestFactory, Module
from .config import config
from .app_controller import AppController
from .app_service import AppService
from src.utils.logging import logger
from src.utils.sessions import Base, engine
from src.sitemap_generator.sitemap_generator_module import SitemapGeneratorModule
from fastapi.middleware.cors import CORSMiddleware
from src.website_generator.website_generator_module import WebsiteGeneratorModule


@Module(
    imports=[SitemapGeneratorModule, WebsiteGeneratorModule],
    controllers=[AppController],
    providers=[AppService],
)
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="This is my Async PyNest app.",
    title="PyNest Application",
    version="1.0.0",
    debug=True,
)
http_server = app.get_server()
http_server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "HEAD", "PUT", "PATCH", "POST", "DELETE", "OPTIONS"],
    allow_headers=[
        "Content-Type",
        "Accept",
        "Authorization",
        "x-skip-toast",
        "sessionid",
    ],
)


@http_server.on_event("startup")
async def startup():

    async def startup():
        logger.info("Tables to be created: %s", Base.metadata.tables.keys())
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Tables after creation: %s", Base.metadata.tables.keys())
