from flask import Flask, render_template, redirect, request
import queries
app = Flask(__name__)


@app.route("/", methods=["GET"])
def route_list():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)