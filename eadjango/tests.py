import unittest
from django.urls import reverse
from django.test import Client
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_post(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["text"] = "text"
    defaults["created_date"] = "created_date"
    defaults.update(**kwargs)
    if "author" not in defaults:
        defaults["author"] = create_'auth_user'()
    return Post.objects.create(**defaults)


class PostViewTest(unittest.TestCase):
    '''
    Tests for Post
    '''
    def setUp(self):
        self.client = Client()

    def test_list_post(self):
        url = reverse('app_name_post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        url = reverse('app_name_post_create')
        data = {
            "title": "title",
            "text": "text",
            "created_date": "created_date",
            "author": create_'auth_user'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_post(self):
        post = create_post()
        url = reverse('app_name_post_detail', args=[post.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        post = create_post()
        data = {
            "title": "title",
            "text": "text",
            "created_date": "created_date",
            "author": create_'auth_user'().pk,
        }
        url = reverse('app_name_post_update', args=[post.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
