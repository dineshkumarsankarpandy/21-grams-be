from nest.core import Controller, Get, Post, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
from .website_generator_service import WebsiteGeneratorService
from .website_generator_model import Sitemap


@Controller("website_generator", tag="website_generator")
class WebsiteGeneratorController:

    def __init__(self, website_generator_service: WebsiteGeneratorService):
        self.website_generator_service = website_generator_service

    @Get("/")
    async def get_website_generator(self, session: AsyncSession = Depends(config.get_db)):
        return await self.website_generator_service.get_website_generator(session)

    @Post("/")
    async def add_website_generator(self, website_generator: Sitemap, session: AsyncSession = Depends(config.get_db)):
        return await self.website_generator_service.add_website_generator(website_generator, session)
    

    
    @Post('/website-generator')

    async def website_generator(self, data: Sitemap):

        try:

            result = await self.website_generator_service.generate_website(data)
            print(result,'<----------------------------')
            return JSONResponse(content =result, status_code=status.HTTP_200_OK)

        except HTTPException as e:

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = f'Internal server error'
                    )


 
