# Generated by Django 5.1.3 on 2024-11-16 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='more_details',
            field=models.TextField(blank=True),
        ),
    ]
