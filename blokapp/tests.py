from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.

class HomepageTestCase(TestCase):
    def test_homepage(self):
        client = Client()

        url = reverse('index')

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')

    def test_addPost(self):
        client = Client()

        url = reverse('store')

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'store.html')
