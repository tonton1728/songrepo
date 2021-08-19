from django.db import models
from django.conf import settings 
from django.core.files.storage import FileSystemStorage
# Create your models here.

partitionsstorage = FileSystemStorage(location=settings.MEDIA_ROOT+'partitions')

class partitions(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ForeignKey('authors', on_delete=models.PROTECT)
    ref = models.CharField(max_length=50, null=True, blank=True)
    types = models.ManyToManyField('types')
    #partition_files = models.FileField(storage=partitionsstorage, blank=True)
    partition_files = models.ManyToManyField('partition_file')

    def __str__(self):
        if self.ref: 
            return "%s - %s - %s "%(self.title, self.ref, self.authors.name)
        else:
            return "%s - %s"%(self.title, self.authors.name)


class authors(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class types(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class partition_file(models.Model):
    partition_file = models.FileField(storage=partitionsstorage)

    def __str__(self):
        return self.partition_file.name

    def url(self):
        return self.partition_file.url.replace(settings.MEDIA_URL, settings.MEDIA_URL+'partitions/')

    def name(self):
        return self.partition_file.name

class playlist(models.Model):
    name = models.CharField(max_length=200)
    partition_list = models.ManyToManyField('partitions')

    def __str__(self):
        return self.name
