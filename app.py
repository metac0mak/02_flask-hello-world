# ---- Flask Hello World ---- #

# import the Flask class from the Flask Module
from flask import Flask

import time

# create the application object
app = Flask(__name__)


# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url

# main hello world app
@app.route("/")
# define the view using a function, which returns a string
def hello_world():
	return "Hey world. . . time is tic toc'ing . . . !?!?!?!?!"


# dynamic route 	--> search
@app.route("/test/<search_query>")
def search(search_query):
	return "Your search query was . .  ." + search_query


# implementing data types

# integers
@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"


# floats
@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correct"


# dynamic route that accepts slashes
# paths
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"


# New View
# dynamic response objects based on route
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name)
	else:
		return "Not Found", 404




if __name__ == "__main__":
	app.run()