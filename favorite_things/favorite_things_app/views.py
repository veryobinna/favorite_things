from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import FavoriteThing, Category
from .serializers import CategorySerializer, FavoriteThingSerializer
import logging


logger = logging.getLogger()


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category, context={"request": request})
        category_fav = Category.objects.filter(pk=pk)
        favorite_things = []
        if category_fav:
            for favorite_thing in category_fav[0].favorite_things.all():
                favorite_things.append(
                    {
                        key: val
                        for key, val in vars(favorite_thing).items()
                        if key != "_state"
                    }
                )
        data = dict(serializer.data)
        data.update({"favorite_things": favorite_things})

        return Response(data)


class FavoriteThingView(viewsets.ModelViewSet):
    queryset = FavoriteThing.objects.all()
    serializer_class = FavoriteThingSerializer

    def create(self, request):
        serializer = FavoriteThingSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            ranking = serializer.validated_data["ranking"]
            category = serializer.validated_data["category"]

            if not FavoriteThing.is_valid_rank(category, ranking):
                return Response(
                    {
                        "error": f"The rank: '{ranking}' must be 1 or a sequential increment of the last rank in the list"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            FavoriteThing.reorder(category, new_ranking=ranking)
            serializer.save()
            logger.info(f"Item created: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Bad request:{serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = FavoriteThing.objects.all()
        favorite_thing = get_object_or_404(queryset, pk=pk)
        serializer = FavoriteThingSerializer(
            instance=favorite_thing, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            new_ranking = int(serializer.validated_data["ranking"])
            category = serializer.validated_data["category"]
            old_ranking = int(favorite_thing.ranking)
            if not FavoriteThing.is_valid_rank(category, new_ranking):
                return Response(
                    {
                        "error": f"The rank: '{new_ranking}' must be a sequential increment of the last rank in the list"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            FavoriteThing.reorder(category, new_ranking, old_ranking)
            serializer.save()
            logger.info(f"Item updated: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Error: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        favorite_thing = FavoriteThing.objects.get(pk=pk)
        ranking = favorite_thing.ranking
        category = favorite_thing.category
        FavoriteThing.reorder(category, old_ranking=ranking)
        favorite_thing.delete()
        logger.info(f"Item deleted: {favorite_thing}")

        return Response(status=status.HTTP_204_NO_CONTENT)
