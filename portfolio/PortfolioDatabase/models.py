from django.db import models

# Create your models here.
class Hobbies(models.Model):

    def __str__(self):
        return self.hobby_name+': ' +self.hobby_description

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default="https://d2rdhxfof4qmbb.cloudfront.net/wp-content/uploads/20200513185709/iStock-1097132584.jpg")





class Portfolio(models.Model):

    portfolio_name = models.CharField(max_length=200)
    portfolio_description = models.CharField(max_length=200)
    portfolio_image = models.CharField(max_length=500, default="https://images2.minutemediacdn.com/image/upload/c_crop,h_1190,w_2121,x_0,y_224/v1554926272/shape/mentalfloss/24832-istock-698876630.jpg?itok=oU5bq3Pj")

    def __str__(self):
        return self.portfolio_name+': ' +self.portfolio_description


