# Generated by Django 5.1.3 on 2024-12-01 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0005_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blogging.category'),
        ),
    ]