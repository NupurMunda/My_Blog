# Generated by Django 2.2.1 on 2019-05-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190519_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]