# Generated by Django 2.2 on 2020-10-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0002_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobbies',
            name='hobby_image',
            field=models.CharField(default='https://www.takeoutlist.com/assets/images/food_default.png', max_length=500),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_image',
            field=models.CharField(default='https://www.takeoutlist.com/assets/images/food_default.png', max_length=500),
        ),
    ]
