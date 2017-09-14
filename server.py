from flask import Flask, render_template, redirect, request
import queries
from constants import COLUMN_ORDERS, ALIASES
app = Flask(__name__)


@app.route("/", methods=["GET"])
def route_list():
    return render_template("index.html")


@app.route("/<query>", methods=["GET"])
def temple(query):
    if query == "mentors":
        result = queries.mentors_and_schools()
    elif query == "all_schools":
        result = queries.all_schools()
    elif query == "mentors_by_country":
        result = queries.mentors_by_country()
    elif query == "contacts":
        result = queries.school_contacts()
    elif query == "applicants":
        result = queries.applicants_after_2016()
    elif query == "applicants_and_mentors":
        result = queries.applicants_and_mentors()

    return render_template("list.html",
                           result=result,
                           key_order=COLUMN_ORDERS[query],
                           key_aliases=ALIASES)

if __name__ == "__main__":
    app.run(debug=True)
