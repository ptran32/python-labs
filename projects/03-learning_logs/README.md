**Learning app with Django**

Web application which allow a user to manage his personal notes:

- CRUD operations on topic
- CRUD operations on notes
- Display topics and related notes
- Register new users
- Authenticate existing users

**Requirements**

- python >= 3.8
- Poetry installed on your laptop ( [https://github.com/python-poetry/poetry](https://github.com/python-poetry/poetry) )

*Access to the application hosted on Heroku*

[https://learning-log-heroku.herokuapp.com/](https://learning-log-heroku.herokuapp.com/)


**Run app**

*Create a new virtual environment*

```
poetry shell
```

*Install project dependencies*

```
poetry install
```

*Init the sqlite database*


```
python manage.py migrate
```

*Run the application*

```
python manage.py runserver
```

*Access to the application*

From your web browser: http://127.0.0.1:8000
