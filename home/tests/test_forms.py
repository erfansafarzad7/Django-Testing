from django.test import TestCase
from home.forms import UserRegisForm
from django.contrib.auth.models import User


class TestRegistrationForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='erfan', email='erfan@email.com', password='erfanpass')

    def test_valid_data(self):
        form = UserRegisForm(data={'username': 'erfan2', 'email': 'erfan2@email.com', 'password1': 'erfanpass', 'password2': 'erfanpass'})
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form = UserRegisForm(data={})
        self.assertFalse((form.is_valid()))
        self.assertEqual(len(form.errors), 4)

    def test_exist_email(self):
        form = UserRegisForm(data={'username': 'erfan', 'email': 'erfan@email.com', 'password1': 'erfanpass', 'password2': 'erfanpass'})
        self.assertEqual(len(form.errors), 1)

    def test_unmatch_passwords(self):
        form = UserRegisForm(data={'username': 'erfan3', 'email': 'erfan3@email.com', 'password1': 'erfanpass', 'password2': 'erfan'})
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error)
