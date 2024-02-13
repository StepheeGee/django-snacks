# in snacks/tests.py

from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render

class SnacksTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('snacks:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('snacks:about'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('snacks:home'))
        self.assertTemplateUsed(response, 'snacks/base.html')
        self.assertTemplateUsed(response, 'snacks/home.html')

    def test_about_page_template(self):
        response = self.client.get(reverse('snacks:about'))
        self.assertTemplateUsed(response, 'snacks/base.html')
        self.assertTemplateUsed(response, 'snacks/about.html')

