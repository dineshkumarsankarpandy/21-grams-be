from nest.core import Controller, Get, Post, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException


from .sitemap_generator_service import SitemapGeneratorService
from .sitemap_generator_model import SitemapGenerator


@Controller("sitemap_generator", tag="sitemap_generator")
class SitemapGeneratorController:

    def __init__(self, sitemap_generator_service: SitemapGeneratorService):
        self.sitemap_generator_service = sitemap_generator_service


    @Post("/")
    async def add_sitemap_generator(self, sitemap_generator: SitemapGenerator, session: AsyncSession = Depends(config.get_db)):
        return await self.sitemap_generator_service.add_sitemap_generator(sitemap_generator, session)
    

    
    @Post("/sitemap-generator")
    async def sitemap_generator(self, data: SitemapGenerator,):
        try:

            result = await self.sitemap_generator_service.generate_sitemap_generator(data)
            print('-----------------------------------')
            print(result)
            return JSONResponse(content=result,status_code=status.HTTP_200_OK)

        except HTTPException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'Internal server error : {str(e)}'
            )   
    


