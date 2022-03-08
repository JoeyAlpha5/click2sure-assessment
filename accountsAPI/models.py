from django.db import models
from userAPI.models import userProfile
# Create your models here.


account_types = [("Savings","Savings"), ("Credit", "Credit")]
transaction_types = [("Deposit","Deposit"), ("Withdrawal", "Withdrawal")]

# account type can either be a savings or credit account
class accountType(models.Model):
    account_type_name = models.CharField(max_length=50, choices=account_types, default="")
    account_type_minimum_balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type_description = models.CharField(max_length=200)
    account_type_created_at = models.DateTimeField(auto_now_add=True)
    account_type_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_type_name

#  bank account model
class account(models.Model):
    account_user = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    account_type = models.ForeignKey(accountType, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_created_at = models.DateTimeField(auto_now_add=True)
    account_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_user.user_profile_user.username


class transaction(models.Model):
    transaction_account = models.ForeignKey(account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50, choices=transaction_types, default="")
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_description = models.CharField(max_length=200)
    transaction_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_description
