from django.db import models

# Create your models here.

class partitions(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ForeignKey('authors', on_delete=models.PROTECT)
    ref = models.CharField(max_length=50, null=True, blank=True)


class authors(models.Model):
    name = models.CharField(max_length=50)
