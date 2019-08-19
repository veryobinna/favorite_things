from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField
from django.db.models import F
from rest_framework.response import Response


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FavoriteThing(models.Model):
    class Meta:
        ordering = ("ranking",)

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, validators=[MinLengthValidator(10)])
    ranking = models.IntegerField(validators=[MinValueValidator(1)])
    category = models.ForeignKey(
        Category, related_name="favorite_things", on_delete=models.CASCADE
    )
    metadata = JSONField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def is_valid_rank(category, ranking):
        last_favorite_thing = (
            FavoriteThing.objects.filter(category=category).order_by("-ranking").first()
        )

        if last_favorite_thing:
            if ranking > last_favorite_thing.ranking + 1:
                return False
        elif ranking != 1:
            return False
        return True

    def reorder(category, new_ranking=0, old_ranking=0):
        if not old_ranking:
            FavoriteThing.objects.filter(
                category=category, ranking__gte=new_ranking
            ).update(ranking=F("ranking") + 1)

        elif not new_ranking:
            FavoriteThing.objects.filter(
                category=category, ranking__gt=old_ranking
            ).update(ranking=F("ranking") - 1)

        elif old_ranking > new_ranking:
            FavoriteThing.objects.filter(
                category=category, ranking__gte=new_ranking, ranking__lt=old_ranking
            ).update(ranking=F("ranking") + 1)
        elif old_ranking < new_ranking:
            FavoriteThing.objects.filter(
                category=category, ranking__gt=old_ranking, ranking__lte=new_ranking
            ).update(ranking=F("ranking") - 1)

    def __str__(self):
        return self.title
