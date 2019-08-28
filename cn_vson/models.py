from django.db import models

class Portfolio(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
