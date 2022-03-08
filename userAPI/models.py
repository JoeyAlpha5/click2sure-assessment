from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

# gender choices
gender_choices = [("Male","Male"), ("Female", "Female"),("Non-Binary", "Non-Binary"),("Other", "Other")]

# User Profile Model contains more information about the user
class userProfile(models.Model):
    user_profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile_phone = models.CharField(max_length=20, blank=True)
    user_profile_address = models.CharField(max_length=200, blank=True)
    user_profile_city = models.CharField(max_length=50, blank=True)
    user_profile_state = models.CharField(max_length=50, blank=True)
    user_profile_zipcode = models.CharField(max_length=10, blank=True)
    user_profile_country = models.CharField(max_length=50, blank=True)
    user_profile_gender = models.CharField(max_length=50, choices=gender_choices, default="")

    def __str__(self):
        return self.user_profile_user.username

    class Meta:
         ordering = ['-id']

def create_user_profile(sender, **kwargs):
    if kwargs["created"]:
        new_user_profile = userProfile.objects.create(user_profile_user=kwargs["instance"])


#listen for when a new user has been created, if so execute the create_user_profile function
post_save.connect(create_user_profile, sender=User)