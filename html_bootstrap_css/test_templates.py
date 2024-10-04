#!/usr/bin/python3
"""Test html file by passing it as the arg.
"""
from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(sys.argv[1])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
