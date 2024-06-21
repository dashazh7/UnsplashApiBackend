from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import models, crud, schemas
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    db_url='postgres://postgres:root@192.168.110.104:5432/unsplash_database',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/favorites/{favorite_id}", response_model=schemas.Favorite)
async def get_favorite(favorite_id: str):
    return await crud.get_favorite(favorite_id)


@app.get("/favorites", response_model=List[schemas.Favorite])
async def get_favorites():
    return await crud.get_favorites()


@app.post("/favorites", response_model=schemas.Favorite)
async def create_favorite(favorite: schemas.FavoriteCreate):
    return await crud.create_favorite(favorite)


@app.delete("/favorites/{favorite_id}", status_code=204)
async def delete_favorite(favorite_id: str):
    await crud.delete_favorite(favorite_id)


@app.put("/favorites/{favorite_id}", response_model=schemas.Favorite)
async def update_favorite(favorite_id: str, favorites_data: schemas.FavoriteBase):
    return await crud.update_favorite(favorite_id, favorites_data)
