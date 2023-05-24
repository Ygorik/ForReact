from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: int
    author: int
    img: str

engine = create_engine("sqlite:///base.db")

SQLModel.metadata.create_all(engine)
