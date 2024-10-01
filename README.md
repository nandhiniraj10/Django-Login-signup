**Project Overview:**<br>

This Django project implements basic user authentication functionality with features like user signup, login, and logout. It interacts with the built-in Django authentication system  ** (django.contrib.auth)**  to manage user sessions securely.<br>

**Main Features:**<br>
**1.Home Page (home view):**<br>This view renders the homepage  **(index.html)** when accessed.<br>
It acts as a simple entry point for the application, without requiring authentication.<br>


**2.User Signup (signup view):**<br>
Users can register by providing a username, password, and confirmation of the password.<br>
Password validation ensures that both **password ** and **confirm_password** match.<br>
It checks if the username already exists and displays relevant messages using Django's messaging framework **(django.contrib.messages)**.<br>
If successful, the user is created and redirected to the login page.<br>

**3.User Login (login_user view):**<br>
Users can log in by providing their username and password.<br>
The **authenticate** method from Django’s authentication system checks if the credentials are valid.<br>
Upon successful login, the user is redirected to the homepage, while failed attempts show an error message and redirect the user back to the logout page.<br>

**4.User Logout (logout_user view):**<br>
This view logs out the currently authenticated user using Django’s **logout** function.<br>
After logging out, the user is redirected back to the homepage.<br>

**Technologies & Tools:**<br>
**Django's Built-in User Model: **The project uses Django's built-in **User** model to manage user credentials and authentication.<br>
**Django Auth System:** The **auth** module is used to handle authentication and session management.<br>
**Messages Framework:** User feedback such as errors or success messages is displayed using Django’s messages framework.<br>
**Potential Improvements:**<br>
Add form validation using Django forms instead of manually handling POST data.<br>
Improve security by adding email verification or password strength validation.<br>
Add flash messages for enhanced user experience when interacting with the app (e.g., showing success/failure messages).
