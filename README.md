
**Accidents**

1) Create a virtual environment in the root directory.<br>
**Command in root directory**
 ```
python -m venv venv
```

3) Activate your virtual environment using <br>
**Command in root directory in Windows**
```
venv\Scripts\activate
```

5) Switch to the bus_tracking directory <br>
**Command in root directory**
```
cd accidents
```

7) Install the packages required for the project using the command. <br>
**Command in bus_tracking directory**
 ```
pip install -r requirements.txt
```

9) Configuring postgres database. <br>
**Use this link to download pgAdmin4**
```
https://www.youtube.com/watch?v=IYHx0ovvxPs
```
Follow the video till the server is set up in pgAdmin4. <br>
1) Create the database by right clicking the databases dropdown under server.  <br>
2) Give the database name and click save. <br>
3) In the django settings look for DATABASE key and replace this with <br>
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "<your database name>",
        "USER": "<user_name>",
        "PASSWORD": "<password>",
        "HOST": "127.0.0.1",
        "PORT": "<port_number>",
    }
}
```
Remember the password and the port number with which you set up the database server. <br>

10) Open the file **load.py** in the **scripts folder** in **app folder**.<br>
11) Change the path of the file **Load_data** in load.py file. You can find these files in the root directory of the repository.<br>
12) Perform migrations and migrate the model to Postgres database.
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
     ```
13) Run the command from navigating to the root project directory in the terminal. <br>
    ```
    python manage.py runscript load
    ```
14) If you require to decide to change the model after setting up the database server use the command prompt in pgAdmin4 using SQL commands to view the metadata of the table. <br>
    Make sure to do changes in Postgres schema using SQL commands then perform migrations on the model and then load the data.<br>
    You can access postgres terminal by clicking the database in the pgAdmin server and then click on the rightmost button **>_** icon to open the terminal. Here you can write SQL commands to change the schema of the database already set up. Access these tables created by migrations using **<app_name>_<model_name>**.<br>


