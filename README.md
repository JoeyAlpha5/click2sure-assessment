# Click2Sure-assessment

This documentation provides a breakdown of the Click2Sure API backend banking application.  The application currently consists of 5 API endpoints. Some of the requirements from the project brief have been left out due to time constraints, but I've highlighted these in the Future improvements section which goes over how I would go about implementing them.

Use the sections listed below to get started with running the application on your machine. 

## Documentation sections
- [Setting up the app](#setting-up-the-app)
- [Third party libraries and packages used](#third-party-libraries)
- [API endpoints](#api-endpoints)
- [Application preview](#application-preview)
- [Future improvements](#future-improvement)



### Third party libraries

This section lists all the third party libraries and dependencies that have been used and the reasons for including them.

1. [Django Rest Framework](https://www.django-rest-framework.org/). The django rest framework simplifies the process of building RestFul APIs, using it helped speed up the process of building the APIs.

3. [Whitenoise](https://pypi.org/project/whitenoise/). Whitenoise has been added to serve static files when loading the app on Heroku.


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

To create a new user, you can use the django default url or append the following to the app url:

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

To create/open a new bank account, append the following to the app url:

```
/account/createAccount
```

Below is an example of the required json object to create a new bank account. To view the list of the users in the database and retrieve user_ids, you can download [DB Browser for SQLite](https://sqlitebrowser.org/).

There are currently two account types, Savings (account_type_id:1) and Credit (account_type_id:2).

The minimum ammount required to open a savings account is R 50.00, passing an amount less than this will return the following error message: *'Savings account cannot have a balance of less than R 50.00'*

The maximum credit limit on a credit account is (R 20 000.00), passing an amount less than this will return the following error message: *'Credit account cannot have a balance of less than R-20000.00'*

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

To make a deposit, append the following to the app url:

```
/account/makeDeposit
```

Below is an example of the required json object to make a deposit. To make a deposit, the user has to be signed in. To view the list of the accounts in the database and retrieve account_ids, you can download [DB Browser for SQLite](https://sqlitebrowser.org/).

```
{
    "account_id":1,
    "deposit_amount":500,
    "transaction_description":"Deposited 500 bucks"
}
```


#### 4. Create/Make Withdrawal Enpoint

To make a withdrawal, append the following to the app url:

```
/account/makeWithdrawal
```

Below is an example of the required json object to make a withdrawal. To make a withdrawal, the user has to be signed in. To view the list of the accounts in the database and retrieve account_ids, you can download [DB Browser for SQLite](https://sqlitebrowser.org/).


```
{
    "account_id":2,
    "withdrawal_amount":10000,
    "transaction_description":"Withdrawing money from credit account"
}
```

#### 5. Get User Account Details Enpoint

To get accounts, balances, and the last 10 transactions, for the logged in USER., append the following to the app url:

```
/account/userAccountDetails
```



### Application Preview

The app has been deployed on Heroku and can be previewed [here](https://click-2-sure.herokuapp.com/).

To login in to the django admin site use the following credentials:

```
username: joey
password: 12345678
```


### Future Improvements

The current application is far from perfect and it is still missing a few features that have been outlined in the project brief. I approached this project by breaking down the requirements listed in the project brief and grouping them into high priority and low priority tasks.

Implementing the CRUD functionality using the django-rest-framework was high priority. 

The following features/functionality have been left out, but I've detailed how I would go about implementing them:

#### 1. CSV export

The Django documentation provides a guideline on how to go about implementing this feature [here](https://docs.djangoproject.com/en/4.0/howto/outputting-csv/). This would have been my starting point, additionally I would have explored other python libararies.

#### 2. Documenting the API

The Django Rest Framework documentation provides steps on how to go about documenting your API using Swagger [here](https://www.django-rest-framework.org/topics/documenting-your-api/). Going through the DRF and Swagger documentation would be my starting point in documenting the API.


#### 3. Seeding my database

To populate my db with dummy data, I would use the [django-seed](https://pypi.org/project/django-seed/) library.


### 4. Test cases

For the sake of time I've not written any test cases for this project. I would use the python unittest module along with the steps outline [here](https://docs.djangoproject.com/en/4.0/topics/testing/overview/) to write my test cases.


#### 5. Interacting with the API using curl commands

This would have been a new and exciting challenge and is definitely something I'll be looking into. The [curl website](https://curl.se/) would be my starting point to familiarise myself with curl commands.


#### Other API improvements

The API enpoints could do with a little more validation. I've only implmented the validation requirements specified in the project brief such as minimun amounts required for specific account types.

Securing the API endpoint would also be of great benefit, currently some of the enpoints do not require the user to be authenticated. For a *'real world'* application with a frontend and a backend, using a method like token based authentication would add an addittional layer of security.



