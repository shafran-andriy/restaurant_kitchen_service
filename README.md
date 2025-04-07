# restaurant_kitchen_service

![DB Structure](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/docs/models.svg)

## 📌 Overview  
**restaurant_kitchen_service** is a web application designed to manage restaurant kitchen operations, including handling cooks, dishes, and dish types.  

## 📸 Screenshots  

### 🔑 Login Page  
![Login Page](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/Login-page.png)

### 🏠 Home Page  
![Home Page](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/Home-page.png)

### 👤 Username Page  
![Username Page](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/Username-page.png)

### 👨‍🍳 All Cooks Page  
![All Cooks Page](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/All_cooks-page.png)

### ➕ Create Cook Page  
![Create Cook Page](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/Create_cook-page.png)

### 🍽️ All Dishes Page  
![All Dishes Page](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/Dish_list-page.png)

### ➕ Create Dish Page  
![Create Dish Page](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/Create_dish-page.png)

### 🍲 All Dish Types Page  
![All Dish Types Page](https://github.com/shafran-andriy/restaurant_kitchen_service/blob/main/photos_of_the_site/Dish_type-page.png)

---

## 🚀 Deployment 

Link to deployed site via render.com:

![restaurant-kitchen-service](https://restaurant-kitchen-service-lp9w.onrender.com/)

Test user:

login: user

password: user12345

## 🚀 Installation & Setup  

### 📥 Clone the Repository  
```sh  
git clone https://github.com/shafran-andriy/restaurant_kitchen_service.git  
cd restaurant_kitchen_service  


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
