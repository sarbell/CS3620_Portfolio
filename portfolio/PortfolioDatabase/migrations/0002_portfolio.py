# Generated by Django 2.2 on 2020-09-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_name', models.CharField(max_length=200)),
                ('portfolio_description', models.CharField(max_length=200)),
            ],
        ),
    ]
