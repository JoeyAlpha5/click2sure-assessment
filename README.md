# Click2Sure-assessment

This documentation provides a breakdown of the Click2Sure API backend banking application.  The application currently consists of 5 API endpoints. Some of the requirements from the project brief have been left out due time constraints, but I've highlighted these in the Future improvements section which goes over how one would go about implementing them.

Use the sections listed below to get started with running the application on your machine. 

## Documentation sections
- [Setting up the app](#setting-up-the-app)
- [Third party libraries and packages use](#third-party-libraries)
- [API endpoints](#api-endpoints)
- [Application Preview](#application-preview)
- [Future improvements](#future-improvement)



### Third party libraries

This section lists all the third party libraries, dependencies that have been used and the reasons for including them.

1. [Django Rest Framework](https://www.django-rest-framework.org/). The django rest framework simplifies the process of building RestFul APIs and given the time constraint using it helped speed up the process of building the blog APIs.

3. [Whitenoise](https://pypi.org/project/whitenoise/). Whitenoise has been added to serve static files when loading the app.


### Setting up the app

1. To get started, clone this repository using the following git command
```
git clone https://github.com/JoeyAlpha5/click2sure-assessment.git
```

2. Once the repo has been cloned, in your terminal cd into the project folder and run the command below to install all the required packages and libraries

```
pip install -r requirements.txt
```

3. You can then run the application by running the following command. The app has been left in debug mode due to time constraints. 

```
python manage.py runserver
```

### API Endpoints

#### 1. Create User Enpoint

To create a new user, you can use the django defualt url or append the following to the app url

```
/user/createUser
```

Below is an example of the required json object to create a new user. The default django User model has been extened with the userProfile model found in [userAPI](https://github.com/JoeyAlpha5/click2sure-assessment/blob/development/userAPI/models.py). When a new user is created a profile for that user containing additional fields such as phone number, address, gender, etc will be created for that user. This has been done in order to illustrate the kind of data a  *'real world'* application would be collecting from users, especially a banking app. The app is far from perfect, additional data that could also be collected would include ID numbers.

```
{
    "user":{
        "username":"Jane",
        "password":"Jane#123"
    },
    "user_profile":{
        "phone":"123456789",
        "address":"14 blo",
        "country":"ZA",
        "city":"JHB",
        "state":"GA",
        "zipcode":"2000",
        "gender":"Female"
    }
}
```

Once the account is created successfully, you can then log in using the username and password you used to create the account.


#### 2. Create Account Enpoint

To create/open a new bank account, append the following to the app url

```
/account/createAccount
```

Below is an example of the required json object to create a new bank account. To view the list of the users in the database and retrieve user_ids, you can download [DB Browser for SQLite](https://sqlitebrowser.org/).

There are currently two account types, Savings (account_type_id:1) and Credit (account_type_id:2).

The minimum ammount required to open a savings account is R 50.00, passing an amount less than this will return the following error message: *'Savings account cannot have a balance of less than R 50.00'*

The maximum credit limit on a credit account is (R 20 000.00). passing an amount less than this will return the following error message: *'Credit account cannot have a balance of less than R-20000.00'*

Savings account json data:

```
{
    "user_id":12,
    "opening_balance":50,
    "account_type_id":1
}
```

Credit account json data:
```
{
    "user_id":12,
    "opening_balance":-10000,
    "account_type_id":2
}
```

#### 3. Create/Make Deposit Enpoint

#### 4. Create/Make Withdrawal Enpoint


#### 5. Get User Account Details Enpoint



