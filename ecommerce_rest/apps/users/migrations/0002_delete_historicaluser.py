# Generated by Django 4.1.3 on 2023-03-15 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalUser',
        ),
    ]