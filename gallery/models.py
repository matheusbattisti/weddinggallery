from django.db import models

from django.contrib.auth.models import User

class Photo(models.Model):

    STATUS = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='static/img/images')
    image = models.ImageField()
    date_taken = models.DateField()
    approved   =  models.CharField(
        max_length=3,
        choices=STATUS,
        default='no'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Like(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo  = models.ForeignKey(Photo, on_delete=models.CASCADE)