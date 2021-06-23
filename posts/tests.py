from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just to test')

    def test_context_data(self):
        post = Post.objects.get(id=1)
        another_text = f'{post.text}'
        self.assertEqual(another_text,'just to test')

class TestHomePageView(TestCase):
    def setUp(self):
        Post.objects.create(text='just to test')

    def test_view_with_url(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code,200)
    
    def test_view_with_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)

    def test_template_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'home.html')
