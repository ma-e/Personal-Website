from django.db import models

class Portfolio(models.Model):
    portfolio_category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/cn/{self.name}"

class Blog(models.Model):
    blog_category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    date = models.DateField()
    author = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f"/cn/{self.title}"

class Bio_img(models.Model):
    name = models.CharField(max_length=100)
    bio_category = models.CharField(max_length=100)
    bio_img = models.ImageField(null=False) 
