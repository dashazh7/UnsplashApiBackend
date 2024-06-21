from tortoise import fields, models


class Favorites(models.Model):
    photo_id = fields.CharField(max_length=255, unique=True)
    photo_url = fields.TextField()
    title = fields.TextField(null=True)
    description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "favorites"

