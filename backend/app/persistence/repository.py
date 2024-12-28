from app.persistence.abstract import IRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from uuid import UUID

class MemoryRepository(IRepository):
    def __init__(self, model):
        self.model = model
    
    async def get(self, obj_id, session: AsyncSession):
        try:
            if isinstance(obj_id, str):
                obj_id = UUID(obj_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for UUID')
        return session.execute(select(self.model).where(obj_id == self.model.id)).scalars().first()

    async def get_all(self, session: AsyncSession):
        return session.execute(select(self.model)).scalars().all()
    
    async def add(self, obj, session: AsyncSession):
        session.add(obj)
        session.commit()
        session.refresh(obj)

        return obj

    async def update(self, obj_id, obj, session: AsyncSession):
        data = obj.dict()
        existing_obj = await self.get(obj_id=obj_id, session=session)
        for key, value in data.items():
            setattr(existing_obj, key, value)

        session.commit()
        session.refresh(existing_obj)
        
        return existing_obj
    
    async def delete(self, obj_id, session: AsyncSession):
        existing_obj = await self.get(obj_id=obj_id, session=session)

        session.delete(existing_obj)
        session.commit()