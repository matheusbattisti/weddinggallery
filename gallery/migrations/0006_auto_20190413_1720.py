# Generated by Django 2.1.4 on 2019-04-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_photo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='approved',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
    ]
