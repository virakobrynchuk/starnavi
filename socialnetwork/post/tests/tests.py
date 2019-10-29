from django.test import TestCase
from django.urls import reverse
from post.models import Post

from django.contrib.auth.models import User


class PostTests(TestCase):

    def setUp(self):
        author = User.objects.create(username='Test_User', password ='testing321')
        Post.objects.create(creator=author, post_title='1', post_text='just a test')

    def test_text_content(self):
        post = Post.objects.get(post_title ='1')
        expected_object_name = f'{post.post_text}'
        self.assertEquals(expected_object_name, 'just a test')

    def test_post_list_view(self):
        response = self.client.get(reverse('Posts'))
        self.assertEqual(response.status_code, 302)
