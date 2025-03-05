from nest.core import Module
from .sitemap_generator_controller import SitemapGeneratorController
from .sitemap_generator_service import SitemapGeneratorService


@Module(
    controllers=[SitemapGeneratorController],
    providers=[SitemapGeneratorService],
    imports=[]
)   
class SitemapGeneratorModule:
    pass

    