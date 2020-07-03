from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group,Permission
from django.core.validators import RegexValidator

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import Permission
# Create your models here.




class News(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    images = models.ImageField(upload_to='tutorial/static/original/', blank=True)
    author = models.ForeignKey('auth.User', related_name='news', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

class Faq(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question    

class Contact(models.Model):
    name= models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254)
    # phone = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+994555555555'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    subject = models.CharField(max_length=60)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()    


