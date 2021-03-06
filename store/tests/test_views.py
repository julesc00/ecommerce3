from unittest import skip

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products


@skip("Show skipping a test")
class TestSkip(TestCase):

    def test_skip_example(self):
        """This is just a skipped test."""
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username="julesc00")
        Category.objects.create(name="django", slug="django")
        Product.objects.create(
            category_id=1,
            title="django Beginners",
            created_by_id=1,
            slug="django-beginners",
            price="20.00",
            image="django"
        )

    def test_url_allowed_hosts(self):
        """Test allowed hosts."""
        response = self.c.get("/")

        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """Test reverse is working; use the slug."""
        response = self.c.get(reverse("store:product_detail", args=["django-beginners"]))

        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """Test Category response status."""
        response = self.c.get(reverse("store:category_list", args=["django"]))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """Test the homepage html."""
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode("utf8")

        self.assertIn("<title>Products Page</title", html)
        self.assertTrue(html.startswith("\n<!doctype html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/product/django-beginners")
        response = all_products(request)
        html = response.content.decode("utf8")

        self.assertIn("<title>Products Page</title", html)
        self.assertTrue(html.startswith("\n<!doctype html>\n"))
        self.assertEqual(response.status_code, 200)
