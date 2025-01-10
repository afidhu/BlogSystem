from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id_user=models.IntegerField()
    profile_image=models.ImageField(upload_to='profile/', default='user.png')
    location=models.CharField(max_length=100)
    bio=models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username
    