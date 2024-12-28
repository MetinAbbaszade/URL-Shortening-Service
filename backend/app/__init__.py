from fastapi import FastAPI
from app.api.v1.endpoints.url import router as url_router
from sqlalchemy import create_engine
from sqlmodel import SQLModel

app = FastAPI()
MYSQL_CONNECTION = 'mysql+pymysql://root:M3tin190534@localhost/Url_Shortener'

engine = create_engine(MYSQL_CONNECTION, echo=True)

def create_app():

    app.include_router(url_router)
    return app

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)