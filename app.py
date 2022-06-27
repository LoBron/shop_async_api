import asyncio
import time

import sqlalchemy as sa
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import pydantic
import databases
from fastapi import FastAPI

DATABASE_URL = 'postgresql+asyncpg://postgres:1@localhost:5432/test'
Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=True)
print('qqqqqqqqqqq')

class Category(Base):
    __tablename__ = 'catalog_category'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(50), nullable=False)
    slug = sa.Column(sa.String(50), unique=True)
    lft = sa.Column(sa.Integer, nullable=False)
    rght = sa.Column(sa.Integer, nullable=False)
    tree_id = sa.Column(sa.Integer, nullable=False)
    level = sa.Column(sa.Integer, nullable=False)
    parent_id = sa.Column(sa.Integer, nullable=True)

class Cat(BaseModel):
    id: int
    name: str
    slug: str
    lft: int
    rght: int
    tree_id: int
    level: int
    parent_id: int

app = FastAPI(title='shop_api')

@app.get("/category/{cat_id}", response_model=Cat)
async def get_cat(cat_id: int):
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        query = select(Category).filtr()


print('uuuuuuu')
async def async_main():
    # engine = create_async_engine(DATABASE_URL, echo=True)
    print('hhhhhhhhhh')

    # Создание таблиц в базе
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    #     await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        query = select(Category).limit(10)
        result = await session.execute(query)
        for cat in result.scalars():
            print(cat.name)

# asyncio.get_event_loop().run_until_complete(async_main())