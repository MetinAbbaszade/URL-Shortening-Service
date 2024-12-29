from app.persistence.abstract import IRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from uuid import UUID

class MemoryRepository(IRepository):
    def __init__(self, model):
        self.model = model
    
    async def get(self, obj_id, session: AsyncSession):
        return session.execute(select(self.model).where(obj_id == self.model.shorten_url)).scalars().first()
    
    async def get_by_id(self, obj_id, session: AsyncSession):
        try:
            if isinstance(obj_id, str):
                obj_id = UUID(obj_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for UUID')
        
        object = session.execute(select(self.model).where(self.model.id == obj_id))
        return object.scalars().first()

    
    async def add(self, obj, session: AsyncSession):
        session.add(obj)
        session.commit()
        session.refresh(obj)

        return obj

    async def update(self, obj_id, obj, session: AsyncSession):
        
        existing_obj = await self.get(obj_id=obj_id, session=session)
        for key, value in obj.items():
            setattr(existing_obj, key, value)

        session.commit()
        session.refresh(existing_obj)
        
        return existing_obj
    
    async def delete(self, obj_id, session: AsyncSession):
        existing_obj = await self.get_by_id(obj_id=obj_id, session=session)

        session.delete(existing_obj)
        session.commit()

    async def update_stats(self, obj_id, session: AsyncSession):
        existing_obj = await self.get_by_id(obj_id=obj_id, session=session)
        data = existing_obj.dict()
        for key, value in data.items():
            if key == 'access_account':
                setattr(existing_obj, key, value + 1)

        session.commit()
        session.refresh(existing_obj)