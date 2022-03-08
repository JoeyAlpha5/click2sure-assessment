from django.shortcuts import render
from .models import userProfile
from django.contrib.auth.models import User
# import API view and response from django_rest_framework which will be used to display results in the browser
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['POST'])
def createUser(request):
    # get the data from the request
    request_data = request.data
    # check if the user and user_profile data is valid
    validate_request = validate_user_data(request_data)
    
    # if the data is valid, create the user and user_profile
    error_in_request = validate_request['error_occured'] == True
    if error_in_request:
        return Response(validate_request['message'])
    else:
        user_data = request_data['user']
        user_profile_data = request_data['user_profile']

        # create and save the user
        user = User.objects.create_user(
            username=user_data['username'], 
            password=user_data['password']
        )
        
        user.save()

        # update the user_profile
        user_profile = userProfile.objects.filter(user_profile_user=user).update(
            user_profile_user=user,
            user_profile_phone=user_profile_data['phone'],
            user_profile_address=user_profile_data['address'],
            user_profile_city=user_profile_data['city'],
            user_profile_state=user_profile_data['state'],
            user_profile_zipcode=user_profile_data['zipcode'],
            user_profile_country=user_profile_data['country'],
            user_profile_gender=user_profile_data["gender"]
        )


    return Response({"message": "User account created successfuly" })



def validate_user_data(request_data):
    error_message = "Unable to create account with the provided information. "
    error_occured = False

    def throw_error():
        error_occured = True
        return {"error_occured": error_occured, "message": error_message}

    # check if the user data and user profile data has been passed
    if 'user' not in request_data or 'user_profile' not in request_data:
        error_message += "Missing user or user_profile data."
        return throw_error()

    user_data = request_data['user']
    user_profile_data = request_data['user_profile']

    # check if the user data is valid
    if "username" not in user_data or "password" not in user_data:
        error_message += "The following fields are required in the user object: username, password"
        return throw_error()

    # check if the user_profile data is valid
    if "phone" not in user_profile_data or "address" not in user_profile_data or "city" not in user_profile_data or "state" not in user_profile_data or "zipcode" not in user_profile_data or "country" not in user_profile_data or "gender" not in user_profile_data:
        error_message += "The following fields are required in the user_profile object: phone, address, country, city, state, zipcode, gender"
        return throw_error()

    # no errors found
    return {"error_occured": error_occured}
    



    