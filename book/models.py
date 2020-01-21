from django.db import models

class Book(models.Model):
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateField()
    sub = models.CharField(max_length=100)
    
    def __str__(self):
        return "<{0}/{1}>".format(self.title,self.writer)