from django.urls import path
from .views import makeDeposit, getUserDetails, createAccount, makeDeposit,makeWithdrawal

urlpatterns=[
    path('makeDeposit',makeDeposit),
    path('makeWithdrawal',makeWithdrawal),
    path('userDetails',getUserDetails),
    path('createAccount',createAccount)
]