# Generated by Django 2.1.4 on 2019-04-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_taken',
            field=models.DateField(),
        ),
    ]
