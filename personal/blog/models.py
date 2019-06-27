from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 140)
	body = models.TextField()#data types
	date = models.DateTimeField() #database back in

	def __str__(self):
		return self.title


