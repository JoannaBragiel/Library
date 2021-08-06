from django.db import models


class Publication_API(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publication_date = models.DateField()
    ISBN_number = models.IntegerField()
    pages = models.IntegerField()
    cover_page = models.ImageField()
    language = models.CharField(max_length=150)

    def __str__(self):
        return self.title