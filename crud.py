from models import Favorites
from schemas import FavoriteCreate, FavoriteBase


async def get_favorite(favorite_id: str):
    return await Favorites.get(photo_id=favorite_id)


async def get_favorites():
    return await Favorites.all()


async def create_favorite(favorites: FavoriteCreate):
    favorite_obj = await Favorites.create(**favorites.dict())
    return favorite_obj


async def delete_favorite(favorite_id: str):
    favorite_obj = await Favorites.get(photo_id=favorite_id)
    await favorite_obj.delete()


async def update_favorite(favorite_id: str, favorites_data: FavoriteBase):
    favorite_obj = await Favorites.get(photo_id=favorite_id)
    await favorite_obj.update_from_dict(favorites_data.dict())
    await favorite_obj.save()
    return favorite_obj
