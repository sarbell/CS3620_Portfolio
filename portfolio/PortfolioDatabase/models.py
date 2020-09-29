from django.db import models

# Create your models here.
class Hobbies(models.Model):

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)

    def __str__(self):
        return self.hobby_name+': ' +self.hobby_description




class Portfolio(models.Model):

    portfolio_name = models.CharField(max_length=200)
    portfolio_description = models.CharField(max_length=200)

    def __str__(self):
        return self.portfolio_name+': ' +self.portfolio_description


