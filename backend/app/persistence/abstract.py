from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    async def get(self, obj_id, db):
        ...
    
    @abstractmethod
    async def add(self, obj, db):
        ...

    @abstractmethod
    async def update(self, obj_id, obj, db):
        ...

    @abstractmethod
    async def delete(self, obj_id, db):
        ...