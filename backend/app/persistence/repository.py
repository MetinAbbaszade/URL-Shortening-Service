from app.persistence.abstract import IRepository


class MemoryRepository(IRepository):
    def __init__(self, model):
        self.model = model
    
    