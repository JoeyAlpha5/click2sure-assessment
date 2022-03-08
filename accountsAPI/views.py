from django.shortcuts import render
from userAPI.models import userProfile
from .models import account, accountType, transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def makeDeposit(request):
    # get the account id, deposit amount and transaction description from the request
    account_id = request.data['account_id']
    deposit_amount = request.data['deposit_amount']
    transaction_description = request.data['transaction_description']

    # get the user's account along with the account type
    get_user_account = account.objects.get(id=account_id)

    # create a transaction object
    new_transaction = transaction(
        transaction_account=get_user_account, 
        transaction_type="Deposit", 
        transaction_amount=deposit_amount, 
        transaction_description=transaction_description
    )
    new_transaction.save()

    # update the balance on the user's account
    get_user_account.account_balance += deposit_amount
    get_user_account.save()


    return Response({"message": "Deposit Successful"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def makeWithdrawal(request):
    # get the account id, deposit amount and transaction description from the request
    account_id = request.data['account_id']
    withdrawal_amount = request.data['withdrawal_amount']
    transaction_description = request.data['transaction_description']

    # get the user's account along with the account type
    get_user_account = account.objects.select_related('account_type').get(id=account_id)

    # check if the user has enough money to make the withdrawal
    remaining_balance_after_withdrawal = get_user_account.account_balance - withdrawal_amount
    user_does_not_have_enough_funds = remaining_balance_after_withdrawal < get_user_account.account_type.account_type_minimum_balance
    if user_does_not_have_enough_funds:
        return Response({"message": "Insufficient funds"})
    else:
        # create a transaction object
        new_transaction = transaction(
            transaction_account=get_user_account, 
            transaction_type="Withdrawal", 
            transaction_amount=withdrawal_amount, 
            transaction_description=transaction_description
        )
        new_transaction.save()

        # update the balance on the user's account
        get_user_account.account_balance -= withdrawal_amount
        get_user_account.save()
    
    return Response({"message": "Withdrawal Successful"})

    


@api_view(['POST'])
def createAccount(request):
    # get request data required for creating account
    user_id = request.data['user_id']
    opening_balance = request.data['opening_balance']
    account_type_id = request.data['account_type_id']
    get_user = userProfile.objects.get(user_profile_user__id=user_id)

    # get account type
    get_account_type = accountType.objects.get(id=account_type_id)
    get_account_type_minimum_balance = get_account_type.account_type_minimum_balance
    get_account_type_name = get_account_type.account_type_name

    # savings account cannot have a balance of less than 50 
    # credit account cannot have a limit of more than 20000
    if opening_balance < get_account_type_minimum_balance:
        return Response({"message": "{} account cannot have a balance of less than {}".format(get_account_type_name, get_account_type_minimum_balance)})

    # create account
    get_user = userProfile.objects.get(user_profile_user__id=user_id)
    get_account_type = accountType.objects.get(id=account_type_id)
    new_account = account(
        account_user=get_user, 
        account_type=get_account_type, 
        account_balance=opening_balance
    )


    new_account.save()

    return Response({"message": "Account created successfully"})

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserDetails(request):
    user = request.user

    return Response({"username": user.username, "email": user.email,"user_id": user.id})