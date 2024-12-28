from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def get(self, obj_id, db):
        ...

    @abstractmethod
    def get_all(self, db):
        ...
    
    @abstractmethod
    def add(self, obj, db):
        ...

    @abstractmethod
    def update(self, obj_id, obj, db):
        ...

    @abstractmethod
    def delete(self, obj_id, db):
        ...