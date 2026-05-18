from django.db import models

# Create your models here.

class Book(models.Model):

    title= models.CharField()
    author = models.CharField()
    price = models.IntegerField()
    pages = models.IntegerField()
    languages = models.CharField()
    Image = models.ImageField(upload_to="books",null=True,blank=True)

    def __str__(self):
        return self.title
