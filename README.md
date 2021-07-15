# Django-Vote-App


# Elect-ron
A Django based enhanced version of https://github.com/YuZaGa/E-Vote-CRUD-App which was made during TechAdrishta's Hackathon(2020).

<h2>Project snapshot</h2>
<img src="./elect.gif?raw=true">

Elect-ron has been developed for college students to cast their votes anytime and from anywhere using browsers. The aim of this web app is to provide convenience to voters as well as officials who monitor the voting process. The app gives election results accurately and instantaneously.

The app has an easy to use interface “Login Screen” for voters where they can login with their College ids. Each voter’s data is stored in database containing their essential information such as College email account id and a voting status which stores whether voter has voted or not. After login, voters have access to voting interface “Voting Screen” that allows them to select candidates for the given positions and submit their voting data securely. Once a voter submits his/her response, then re-submission will not be permissible. Thus, Elect-ron ensures that there is no bogus or fake voting in the elections.

It makes the work of poll admins easy as well with the feature of bulk import of users through CSV, XLXS etc files. This way only eligible candidates can vote in an election.

## Features
1. Poll CRUD Functionalities
2. Bulk import eligible users through external files
3. OTP Login(WIP)
4. Option to display results to all/only admin




<h2>Prerequisites</h2>
<code>See the requirements.txt file</code>

## Setup
1. Git Clone this project:
2. Create an python environment with ```python -m venv venv``` or ```virtualenv venv``` and activate it with (windows:```venv\Scripts\activate```, Mac/Linux:```source venv/bin/activate```.
3. Install required packages: ``` pip install -r requirements.txt ```
4. Create superuser
5. Run app: ``` python manage.py runserver ```
6. Then go to http://127.0.0.1:8000/home in your browser

Bonus - Publish it on Heroku.

https://codeburst.io/deploy-your-django-project-for-free-140d73a2c76b

The free tier of Heroku sleeps after 30 minutes of inactivity. Use Kaffiene (http://kaffeine.herokuapp.com/) to keep it awake. 

## To-Do
1. Implement Django-otp module for 2-factor authentication. 
2. Remove the login bug.

## Credentials
 - username-admin
 - password - adminpassword

## Addition and Modification
Due credit to people who have worked on different components of the project beforehand. **Mahmud Alam**
