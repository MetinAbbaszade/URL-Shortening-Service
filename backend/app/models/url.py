from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class URL(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    url: str = Field(description='Long Url')
    shorten_url: str = Field(description='Shorten Url')
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    access_account: int = Field(description='Access Account')

    def update(self, data):
        for key,value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'shorten_url': self.shorten_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }