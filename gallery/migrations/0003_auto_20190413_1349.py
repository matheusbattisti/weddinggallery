# Generated by Django 2.1.4 on 2019-04-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20190413_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_taken',
            field=models.DateTimeField(),
        ),
    ]