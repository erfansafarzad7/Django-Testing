from django.test import TestCase
from home.models import Writer
from model_bakery import baker


class TestWriterModel(TestCase):
    def test_model_str(self):
        writer = baker.make(Writer)
        self.assertEqual(str(writer), f'{writer.first_name} - {writer.last_name}')
