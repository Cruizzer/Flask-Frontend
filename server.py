from types import NoneType
from unicodedata import name
from webbrowser import get
from flask import Flask, redirect, url_for, render_template, request
from script import function

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def form():
        text = request.form.get("text")
        language = request.form.get("language")

        # Runs a function/script and return value in output
        output = function(text, language)

        # Renders output in index.html
        return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug = True)