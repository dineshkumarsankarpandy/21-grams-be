from nest.core import Module
from .website_generator_controller import WebsiteGeneratorController
from .website_generator_service import WebsiteGeneratorService


@Module(
    controllers=[WebsiteGeneratorController],
    providers=[WebsiteGeneratorService],
    imports=[]
)   
class WebsiteGeneratorModule:
    pass

    