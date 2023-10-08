from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "This is the index page"

@app.get("/aboutme")
def aboutme():
    me = {
        "first_name":"Irvin",
        "last_name": "Zavala",
        "hobbies":"Sleep",
        "is_active":True
    }
    return me