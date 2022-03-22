# swagger

Swagger and Flask exercises

# Exercise 0

On this exercise the only goal is to create your first local webpage using python and flask.
Run the following commands inside the exercise folder:

>pip install -r requirements.txt

>python main.py

Then open a url on http://localhost:99


# Exercise 1

On this exercise the only goal is to create your first API where you will invoke different services internally

>pip install -r requirements.txt

>python main.py

Then open a url on http://localhost:99/form

# Exercise 2

On this exercise the only goal is to create your first API around a docker file

>docker build --tag python-docker .

>docker run -p 5000:5000 python-docker

Then open a url on http://localhost:5000/form

# Exercise 3

Let's explore swagger together

>docker build -t swagger_server .

>docker run -p 8080:8080 swagger_server

Then open a url on http://localhost:8080/v2/ui/#/store

# Exercise 4

Now we both work together

Let's play Blackjack!!!