# Generated by Django 2.2 on 2020-10-02 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0003_auto_20201002_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbies',
            name='hobby_image',
            field=models.CharField(default='https://d2rdhxfof4qmbb.cloudfront.net/wp-content/uploads/20200513185709/iStock-1097132584.jpg', max_length=500),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_image',
            field=models.CharField(default='https://images2.minutemediacdn.com/image/upload/c_crop,h_1190,w_2121,x_0,y_224/v1554926272/shape/mentalfloss/24832-istock-698876630.jpg?itok=oU5bq3Pj', max_length=500),
        ),
    ]