**Simple API using Flask**

![Image of code](https://raw.githubusercontent.com/ptran32/python-labs/master/projects/01_flask_minimal_api/img/flask_mininal_api_code.png)

**Requirements**

- python >= 3.5
- Poetry installed on your laptop ( [https://github.com/python-poetry/poetry](https://github.com/python-poetry/poetry) )


**Run app without docker**

*Create a new virtual environment*

`poetry shell`

*Install project dependencies*

`poetry install`

*Start the web server*
in flask_minimal_api folder, run:

`python main.py`


**Run app with docker**

```
docker build -t flask_minimal_api .
```

```
docker run -p 5000:5000 flask_minimal_api

```

*API usage*

Open a new terminal

*GET all users*
`curl http://localhost:5000/all_users`

*GET a user with id 1*
`curl http://localhost:5000/user/1`

*PUT a user with a new id*
`curl -XPUT http://localhost:5000/user/9 -d "data=bob"`
