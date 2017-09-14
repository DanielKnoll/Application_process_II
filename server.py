from flask import Flask, render_template, redirect, request
import os
import queries
from constants import COLUMN_ORDERS, ALIASES
app = Flask(__name__)


@app.route("/", methods=["GET"])
def route_list():
    return render_template("index.html")


@app.route("/<query>", methods=["GET"])
def temple(query):
    message = ""
    result = ""
    if query == "mentors":
        result = queries.mentors_and_schools()
    elif query == "all_school":
        result = queries.all_schools()
    elif query == "mentors_by_country":
        result = queries.mentors_by_country()
    elif query == "contacts":
        result = queries.school_contacts()
    elif query == "applicants":
        result = queries.applicants_after_2016()
    elif query == "applicants_and_mentors":
        result = queries.applicants_and_mentors()
    elif query == "mentors_full_name":
        result = queries.get_mentors_full_name()
    elif query == "mentors_nick_from_miskolc":
        result = queries.get_mentor_nicks_from_miskolc()
    elif query == "carols_number":
        result = queries.get_me_carols_number()
    elif query == "hat_owner":
        result = queries.carol_dumped_me_give_me_any_other_girls_number()
    elif query == "add_markus":
        query = "all_appl"
        result = queries.get_markus_info()
        if not result:
            queries.get_markus_into_the_system()
            result = queries.get_markus_info()
    elif query == "jemimas_new_number":
        query = "all_appl"
        result = queries.update_jemimas_number()
    elif query == "mauriseu_guys_leaving":
        query = "all_appl"
        """ids = queries.get_mauriseu_guys_id()
        print(ids)
        if ids:
            queries.kick_that_mauriseu_guys_out_updated(ids)
        message = "They are out."""
        message = "Function under construction."

    return render_template("list.html",
                           result=result,
                           key_order=COLUMN_ORDERS[query],
                           key_aliases=ALIASES,
                           message=message)


@app.route("/reset", methods=["GET"])
def reset():
    os.system("psql -f application_process_sample_data_2.sql")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
