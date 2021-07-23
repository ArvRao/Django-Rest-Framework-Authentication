# Django-Rest-Framework-Authentication
This project explains working of Django's Rest framework authentication system. We do API authentication using JWT tokens. We create a custom user class that modifies existing Django's base User class to login using email.



Step 1: 
Run the virtual Environment:

source env/bin/activate

Step 2: Install all dependencies:
cd authtutorial

pip install -r requirements.txt

Step 3: Run the migrations and create database

python3 manage.py makemigrations

python3 manage.py migrate

Step 4: Run the server

python3 manage.py runserver


Tutorial:
Register users by providing their name, unique email and password.

![image](https://user-images.githubusercontent.com/47332035/126826369-57eab90c-4973-47a3-9097-1d31d5809332.png)


User login:


![image](https://user-images.githubusercontent.com/47332035/126826689-967d866b-d87d-48e5-bca3-37421ff9ef81.png)


A unique JWT token is generated if valid credentials are passed. We create a custom cookie variable to store a token inside it.

And finally the logout view. Here the cookie is completely destroyed using the built-in delete_cookie method.

![image](https://user-images.githubusercontent.com/47332035/126827480-353bdf59-fb96-421b-abcd-3b1bab9fc798.png)

Finally the cookie is destroyed when the user logs out of the application.


Hope you found this helpful. Hope you love it.
Cheers!
