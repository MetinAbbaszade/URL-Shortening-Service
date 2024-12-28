from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime


class UrlModel(BaseModel):
    id: UUID | None = uuid4()
    url: str
    shorten_url: str | None = None
    created_at: datetime | None = datetime.now()
    updated_at: datetime | None = datetime.now()