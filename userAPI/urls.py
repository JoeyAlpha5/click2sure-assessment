from django.urls import path
from .views import createUser

urlpatterns = [
    path('createAccount', createUser)
]

