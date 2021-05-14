# Coach dashboard

This is the second project assigned to me as part of Platzi Master to help improve the tech skills as a backend developer. It is a dashboard that lists the coaches for the Platzi Master program.

If you are a coach, you must ask the admin to add you to the platform and then you will be able to access this dashboard, where you can access the list of the coaches currently active in Platzi Master and some of their information, including name, last name, email, phone #, location, role in Platzi Master and a brief desription of the coach's trajecory.

You must have admin credentials in order for you to be able to edit the users and the coaches un the app. A user profile must be created prior to adding a coach, and the SQLite database was used to store the data. The app was intended to use a relational database.

Django (version 3.11.0) was the framework used to develop the app, along with Bootstrap. Bootstrap's CDN was used in order to be able to use this framework without having to install it. A virtual environment would also be a good choice, since this is a very simple app.

This app can be improved by adding options to store images and, if it grows, connecting it to another database engine.

To run this app, you can do it inside a virtual environment. Once active, you need to install Django 3.11.0 and clone the repository in the same folder. After that, you will be able to run the server using the Command Line Interface and running the command "python manage.py runserver" if you are in Windows and "python3 manage.py runserver" in Linux and Mac. A local server will initialize in the local host "127.0.0.1:8000". Open a web browser and you will be ready to go.
