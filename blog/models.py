from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80)
    short_description = models.CharField(max_length=80, null=True, blank=True)
    body = models.TextField()
    featured_pic = models.ImageField(upload_to="cover/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model): 
    subject = models.CharField(max_length=100)
    email = models.EmailField() 
    sender = models.CharField(max_length=80)
    detail = models.TextField()

    def __str__(self):
        return self.subject

    







