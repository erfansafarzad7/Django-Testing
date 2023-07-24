from django.db import models


class Writer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
