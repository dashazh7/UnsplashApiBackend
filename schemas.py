from typing import Optional

from pydantic import BaseModel, constr

class FavoriteBase(BaseModel):
    photo_id: Optional[constr(max_length=255)]
    photo_url: str
    title: str | None = None
    description: str | None = None


class FavoriteCreate(FavoriteBase):
    pass


class Favorite(FavoriteBase):
    id: int

