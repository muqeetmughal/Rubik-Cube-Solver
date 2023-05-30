from flask import Flask, render_template, redirect
from script import main

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/solve", methods=["GET"])
def solve():
    main()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
