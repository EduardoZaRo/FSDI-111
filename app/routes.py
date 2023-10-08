from flask import Flask

app = Flask(__name__)

@app.get("/aboutme")
def index():
    me = {
        "first_name":"Irvin",
        "last_name": "Zavala",
        "hobbies":"Sleep",
        "is_active":True
    }
    return me