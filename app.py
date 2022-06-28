import asyncio
import time
from decimal import Decimal
from typing import Union, Optional
import sqlalchemy as sa
from pydantic import BaseModel
from sqlalchemy import null

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker, relationship

import databases

from fastapi import FastAPI


DATABASE_URL = 'postgresql+asyncpg://postgres:1@localhost:5432/test'
engine = create_async_engine(DATABASE_URL, echo=True)
print('qqqqqqqqqqq')

app = FastAPI(title='shop_api')


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