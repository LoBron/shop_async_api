from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app import engine, app
from models import Cat, Category, Prod, Product


@app.get("/category/{cat_id}", response_model=Cat)
async def get_cat(cat_id: int):
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        cat = await session.get(Category, cat_id)
        return {'id': cat.id,
                'name': cat.name,
                'slug': cat.slug,
                'lft': cat.lft,
                'rght': cat.rght,
                'tree_id': cat.tree_id,
                'level': cat.level,
                'parent_id': cat.parent_id}

@app.get("/product/{prod_id}", response_model=Prod)
async def get_prod(prod_id: int):
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        prod = await session.get(Product, prod_id)
        return {
            'id': prod.id,
            'category_id': prod.category_id,
            'name': prod.name,
            'slug': prod.slug,
            'description': prod.description,
            'price': prod.price,
            'availability': prod.availability,
            'amount': prod.amount,
            'main_photo': prod.main_photo,
            'additional_photo_01': prod.additional_photo_01,
            'additional_photo_02': prod.additional_photo_02,
            'additional_photo_03': prod.additional_photo_03,
        }