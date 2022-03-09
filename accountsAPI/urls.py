from django.urls import path
from .views import makeDeposit, getUserAccountDetails, createAccount, makeDeposit,makeWithdrawal

urlpatterns=[
    path('makeDeposit',makeDeposit),
    path('makeWithdrawal',makeWithdrawal),
    path('userAccountDetails',getUserAccountDetails),
    path('createAccount',createAccount)
]