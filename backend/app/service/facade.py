from sqlalchemy.ext.asyncio import AsyncSession
from app.persistence.repository import MemoryRepository
from app.models.url import URL


class Facade:
    def __init__(self):
        self.url_repo = MemoryRepository(URL)

    async def get_url(self, url_id, db: AsyncSession):
        url = await self.url_repo.get(obj_id=url_id, session=db)
        url_dict = url.dict()
        data = {}
        for key, value in url_dict.items():
            if key is not 'access_account':
                data.setdefault(key, value)
        return data

    async def get_url_stats(self, url_id, db: AsyncSession):
        return await self.url_repo.get(obj_id=url_id, session=db)
    
    async def add_url(self, url, db: AsyncSession):
        await self.url_repo.add(obj=url, session=db)
        return url

    async def update_url(self, url_id, url, db: AsyncSession):
        new_update_data = url.dict()
        update_data = URL(**new_update_data)
        await self.url_repo.update(obj_id=url_id, obj=update_data, session=db)

        return update_data
    
    async def delete_url(self, url_id, db: AsyncSession):
        return await self.url_repo.delete(obj_id=url_id, session=db)
    
    async def update_stat(self, url_id, db: AsyncSession):
        return await self.url_repo.update_stats(obj_id=url_id, session=db)