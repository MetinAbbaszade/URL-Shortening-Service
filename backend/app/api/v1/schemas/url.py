from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
import string
from fastapi import Query
import random
from urllib.parse import urlparse


class UrlModel(BaseModel):
    id: UUID | None = uuid4()
    url: str
    shorten_url: str | None = None
    created_at: datetime | None = datetime.now()
    updated_at: datetime | None = datetime.now()

class FullUrlModel(BaseModel):
    id: UUID | None = uuid4()
    url: str
    shorten_url: str | None = None
    created_at: datetime | None = datetime.now()
    updated_at: datetime | None = datetime.now()
    access_account: int


def generate_short_random_url(length=6):
    data = string.ascii_letters + string.digits
    return ''.join(random.choice(data) for _ in range(length))

def generate_short_url(url):
    domain = urlparse(url)
    path = domain.path
    parts = path.strip("/").split("/") 
    first_endpoint = parts[0] if parts else None

    return first_endpoint