# Generated by Django 2.1.4 on 2019-04-14 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20190413_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
