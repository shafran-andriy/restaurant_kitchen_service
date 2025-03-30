"# restaurant_kitchen_service" 

DB structure:

![image]([https://github.com/user-attachments/assets/634a70ad-0304-485a-9f5d-7ddd49f5162e](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/docs/models.svg))

Pages images:

1. Login page:

![image](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/Login-page.png)

2. 
✨ How to use it

Download the code

$ # Get the code

$ git clone https://github.com/shafran-andriy/restaurant_kitchen_service.git

$ cd restaurant_kitchen_service

👉 Set Up for Unix, MacOS

Install modules via VENV

$ virtualenv env

$ source env/bin/activate

Set Up Database

$ python manage.py makemigrations

$ python manage.py migrate

Start the app

$ python manage.py runserver

At this point, the app runs at http://127.0.0.1:8000/.


👉 Set Up for Windows

Install modules via VENV (windows)

$ virtualenv env

$ .\env\Scripts\activate

Set Up Database

$ python manage.py makemigrations

$ python manage.py migrate

Start the app

$ python manage.py runserver

At this point, the app runs at http://127.0.0.1:8000/.

Use the following command to load prepared data from fixture to test and debug your code:

**python manage.py loaddata taxi_service_db_data.json**

After loading data from fixture you can use following superuser (or create another one by yourself):

**Login: admin.user**

**Password: 1qazcde3**

Feel free to add more data using admin panel, if needed.
