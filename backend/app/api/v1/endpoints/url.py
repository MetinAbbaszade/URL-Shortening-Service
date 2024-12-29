from fastapi import APIRouter, status, Depends, HTTPException
from app.api.v1.schemas.url import UrlModel, FullUrlModel
from app.models.url import URL as urlobject
from app.extensions import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.schemas.url import generate_short_url, generate_short_random_url
from app.service import facade
from urllib.parse import urlparse

router = APIRouter(prefix='/api/v1/url', tags=['url'])

@router.post('/shorten', status_code=status.HTTP_201_CREATED, response_model=UrlModel)
async def create_short_url(url: str, db: AsyncSession = Depends(get_db), random: bool = False):
    if random == True:
        shorten_url = generate_short_random_url()
    else:
        shorten_url = generate_short_url(url=url)

    data = urlobject(url=url, shorten_url=shorten_url)
    await facade.add_url(url=data, db=db)
    return data.to_dict()
        

@router.get('/shorten/{shorten_url}', response_model=UrlModel, status_code=status.HTTP_200_OK)
async def get_url(shorten_url: str, db: AsyncSession = Depends(get_db)):
    url: urlobject = await facade.get_url(url_id=shorten_url, db=db)
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Url not found'
        )
    await facade.update_stat(url_id=url.get('id'), db=db)

    return url

@router.get('/shorten/{shorten_url}/stats', response_model=FullUrlModel, status_code=status.HTTP_200_OK)
async def get_stats(shorten_url: str, db: AsyncSession = Depends(get_db)):
    url = await facade.get_url_stats(url_id=shorten_url, db=db)

    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Url not found'
        )
    
    return url


@router.delete('/shorten/{shorten_url}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_url(shorten_url: str, db: AsyncSession = Depends(get_db)):
    url = await facade.get_url(url_id=shorten_url, db=db)
    if not url:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Url not found'
        )
    await facade.delete_url(url_id=url.get('id'), db=db)


