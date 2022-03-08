from django.contrib import admin
from .models import userProfile
# Register your models here.

# define the display of the userProfile model in the admin interface
class userProfileAdmin(admin.ModelAdmin):
    list_display = ['user_profile_user','user_profile_phone','user_profile_gender','user_profile_zipcode']


admin.site.register(userProfile, userProfileAdmin)