from django.db import models


# Men() --> class (camelCase)
# start_date, run(), walk() --> snake_case
# DATABASES --> constant

class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()

    def __str__(self):
        return self.title



