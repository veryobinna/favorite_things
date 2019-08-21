from django.test import TestCase, Client
from .models import Category, FavoriteThing
import json


class TestModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Places")

    def test_create_category(self):
        category = Category.objects.create(name="Music")

        query = Category.objects.filter(name="Music")
        self.assertEqual(query[0].name, category.name)

    def test_create_favorite_things(self):
        favorite_thing = FavoriteThing.objects.create(
            title="Austria", ranking=1, category=self.category
        )

        query = FavoriteThing.objects.filter(title="Austria")
        self.assertEqual(query[0], favorite_thing)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.category = Category.objects.create(name="Places")
        self.favorite_thing = FavoriteThing.objects.create(
            title="Austria", ranking=1, category=self.category
        )

    def test_returns_categories(self):
        response = self.client.get("/category/")
        resp = json.loads(response.content)
        category = resp["results"][0]

        self.assertEqual(category["name"], self.category.name)
        self.assertEqual(response.status_code, 200)

    def test_returns_categories(self):
        response = self.client.get("/favorite_things/")
        resp = json.loads(response.content)
        favorite_thing = resp["results"][0]

        self.assertEqual(favorite_thing["title"], self.favorite_thing.title)
        self.assertEqual(response.status_code, 200)

    def test_add_category(self):
        category = {"name": "sports"}
        response = self.client.post("/category/", category)
        resp = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(category["name"], resp["name"])

    def test_add_favorite_thing(self):
        favorite_thing = {"title": "Paris", "ranking": 2, "category": self.category.id}
        response = self.client.post("/favorite_things/", favorite_thing)
        resp = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(favorite_thing["title"], resp["title"])

    def test_add_favorite_thing(self):
        favorite_thing = {"title": "Paris", "ranking": 2, "category": self.category.id}
        response = self.client.post("/favorite_things/", favorite_thing)
        resp = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(favorite_thing["title"], resp["title"])

    def test_add_favorite_thing_returns_error_for_invalid_data(self):
        favorite_thing = {"title": "Paris", "ranking": 0, "category": self.category.id}
        response = self.client.post("/favorite_things/", favorite_thing)
        resp = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            resp["ranking"][0], "Ensure this value is greater than or equal to 1."
        )

    def test_update_favorite_thing(self):
        data = {"title": "Lagos", "ranking": 1, "category": self.category.id}
        response = self.client.put(
            f"/favorite_things/{self.favorite_thing.id}/",
            data,
            content_type="application/json",
        )
        resp = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(resp["title"], "Lagos")

    def test_favorite_thing_reorder_on_new_addition(self):
        data = {"title": "London", "ranking": 1, "category": self.category.id}
        response = self.client.post(f"/favorite_things/", data)
        resp = json.loads(response.content)

        prev_top_rank_query = FavoriteThing.objects.filter(title="Austria")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(resp["ranking"], 1)

        self.assertEqual(prev_top_rank_query[0].ranking, 2)

    def test_delete_favorite_thing(self):
        response = self.client.delete(f"/favorite_things/{self.favorite_thing.id}/")
        self.assertEqual(response.status_code, 204)
