from rest_framework import serializers
from .models import FavoriteThing, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "url"]


class FavoriteThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteThing
        fields = [
            "id",
            "title",
            "description",
            "ranking",
            "category",
            "metadata",
            "created_at",
            "updated_at",
            "url",
        ]
