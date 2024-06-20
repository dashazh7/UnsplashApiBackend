from pydantic import BaseModel


class FavoriteBase(BaseModel):
    photo_id: str
    photo_url: str
    title: str
    description: str


class FavoriteCreate(FavoriteBase):
    pass


class Favorite(FavoriteBase):
    id: int

