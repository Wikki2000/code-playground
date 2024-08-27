from flask import Flask, session, redirect, url_for
from os import getenv

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("FLASK_SECRET_KEY")

@app.route("/set-data")
def set():
    session["name"] = {"name": "Wisdom"}
    return redirect(url_for("get"))

@app.route("/get-data")
def get():
    name = session.get("name")
    return f"My name is {name}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
