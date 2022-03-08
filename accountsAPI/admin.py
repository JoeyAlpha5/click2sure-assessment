from django.contrib import admin
from .models import account, accountType, transaction
# Register your models here.

# define the display of the accounts table in the admin interface
class accountAdmin(admin.ModelAdmin):
    list_display = ['account_user','account_type','account_balance', 'account_updated_at','account_created_at']
    ordering = ['-account_created_at']

#  define the display of the account Types table in the admin interface
class accountTypeAdmin(admin.ModelAdmin):
    list_display = ['account_type_name','account_type_minimum_balance','account_type_description','account_type_created_at','account_type_updated_at']
    ordering = ['-account_type_created_at']


# define the display of the transactions table in the admin interface
class transactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_account','transaction_type','transaction_amount','transaction_created_at']
    ordering = ['-transaction_created_at']


admin.site.register(account, accountAdmin)
admin.site.register(accountType, accountTypeAdmin)
admin.site.register(transaction, transactionAdmin)