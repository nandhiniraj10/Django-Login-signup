This Django project implements basic user authentication with signup, login, and logout functionality. It uses Django's built-in User model and authentication system to manage user sessions.

**Home Page:** Renders a simple homepage (index.html).
**Signup:** Allows users to register by providing a username and password. It checks if passwords match and if the username is already taken. Success or error messages are displayed using Django's messages framework.
**Login:** Authenticates users with a username and password. If valid, they are logged in and redirected to the homepage.
**Logout:** Logs users out and redirects them to the homepage.
The project uses Django's auth and messaging systems to provide feedback and manage user sessions.
