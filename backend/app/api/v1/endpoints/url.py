from fastapi import APIRouter, status, Depends
from app.api.v1.schemas.url import Url, UrlModel
from app.extensions import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/api/v1/url', tags=['url'])

@router.post('/shorten', response_model=UrlModel, status_code=status.HTTP_201_CREATED)
def create_short_url(url: Url, db: AsyncSession = Depends(get_db)):
    ...

@router.get('/shorten/{shorten_ur}')
def get_url():
    ...

@router.put('/shorten/{shorten_url}')
def update_url():
    ...

@router.delete('/shorten/{shorten_url}')
def delete_url():
    ...

@router.get('/shorten/{shorten_url}/stats')
def get_stats():
    ...