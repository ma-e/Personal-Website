from django.db import models

class Portfolio(models.Model):
    portfolio_category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/{self.name}"

class Blog(models.Model):
    blog_category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    date = models.DateField()
    author = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f"/{self.title}"

class Bio(models.Model):
    name = models.CharField(max_length=100)
    bio_category = models.CharField(max_length=100)
    bio_img = models.ImageField() 
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/{self.name}"

class Portfolio(models.Model):
    portfolio_category = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    portfolio_img = models.ImageField()
    date = models.DateField()
    
    def __str__(self):
        return self.portfolio_category
    def get_absolute_url(self):
        return f"/portfolio/{self.portfolio_category}"

class Portfolio_game(models.Model):
    name = models.CharField(max_length=100)
    portfolio_category = models.CharField(max_length=100)
    bio_img = models.ImageField()
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/{self.name}"

class Portfolio_painting(models.Model):
    name = models.CharField(max_length=100)
    portfolio_category = models.CharField(max_length=100)
    bio_img = models.ImageField()
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/{self.name}"

class Portfolio_photo(models.Model):
    name = models.CharField(max_length=100)
    portfolio_category = models.CharField(max_length=100)
    bio_img = models.ImageField()
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/{self.name}"

class Portfolio_other(models.Model):
    name = models.CharField(max_length=100)
    portfolio_category = models.CharField(max_length=100)
    bio_img = models.ImageField()
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/{self.name}"

class Comment(models.Model):
    name = models.CharField(max_length=100,null=True)
    email= models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=500,null=True)
    blog = models.CharField(max_length=100,null=True)
    date = date = models.DateField(auto_now_add=True, blank=True)


class Project(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=500,null=True)
    project_img = models.ImageField()
    date = date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/{self.name}"