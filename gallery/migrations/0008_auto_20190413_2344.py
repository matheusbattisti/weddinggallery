# Generated by Django 2.1.4 on 2019-04-14 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Photo'),
        ),
    ]
