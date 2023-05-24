from sqlmodel import Session, select
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from db import Book, engine

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/books")
async def get_all_books():
    with Session(engine) as session:
        sel = select(Book)
        books = session.exec(sel).all()
        print(books)
    return books 


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
