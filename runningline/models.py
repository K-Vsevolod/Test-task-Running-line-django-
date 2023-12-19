from django.db import models

# Create your models here.


class History(models.Model):
    def __str__(self):
        return self.text

    text = models.CharField(max_length=100)
