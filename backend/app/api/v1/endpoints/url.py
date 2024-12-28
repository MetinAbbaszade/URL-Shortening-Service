from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/url', tags=['url'])

@router.post('/shorten')
def create_short_url():
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