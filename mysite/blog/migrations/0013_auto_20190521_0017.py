# Generated by Django 2.2.1 on 2019-05-20 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blogpost_dislikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
