from django.test import SimpleTestCase
from django.urls import resolve, reverse
from home.views import Home, About


class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('home:home')
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_about(self):
        url = reverse('home:about', args=('erfan', ))
        self.assertEqual(resolve(url).func.view_class, About)

# python manage.py test
