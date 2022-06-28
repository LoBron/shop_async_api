from typing import Union
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DECIMAL, BOOLEAN
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = 'catalog_category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    slug = Column(String(50), unique=True)
    lft = Column(Integer, nullable=False)
    rght = Column(Integer, nullable=False)
    tree_id = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    parent_id = Column(Integer, nullable=True)
    children = relationship("Product")


class Cat(BaseModel):
    id: int
    name: str
    slug: str
    lft: int
    rght: int
    tree_id: int
    level: int
    parent_id: Union[int, None]


class Product(Base):
    __tablename__ = 'catalog_product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("catalog_category.id"))
    name = Column(String(100))
    slug = Column(String(100))
    description = Column(Text, nullable=True)
    price = Column(DECIMAL(7, 2), default=0)
    availability = Column(BOOLEAN, default=True)
    amount = Column(Integer, default=1)
    main_photo = Column(String)
    additional_photo_01 = Column(String, nullable=True)
    additional_photo_02 = Column(String, nullable=True)
    additional_photo_03 = Column(String, nullable=True)


class Prod(BaseModel):
    id: int
    category_id: int
    name: str
    slug: str
    description: Union[str, None]
    price: float  #Decimal
    availability: bool
    amount: int
    main_photo: str
    additional_photo_01: Union[str, None]
    additional_photo_02: Union[str, None]
    additional_photo_03: Union[str, None]