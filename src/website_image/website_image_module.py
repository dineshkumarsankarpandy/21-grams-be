from nest.core import Module
from .website_image_controller import WebsiteImageController
from .website_image_service import WebsiteImageService


@Module(
    controllers=[WebsiteImageController],
    providers=[WebsiteImageService],
    imports=[]
)   
class WebsiteImageModule:
    pass

    