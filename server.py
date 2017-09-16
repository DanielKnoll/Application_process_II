from flask import Flask, render_template, redirect, request
import os
import queries
from constants import COLUMN_ORDERS, ALIASES, DESC
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
        result = add_markus()
    elif query == "jemimas_new_number":
        result = queries.update_jemimas_number()
    elif query == "mauriseu_guys_leaving":
        queries.kick_that_mauriseu_guys_out_updated("Do not fetch")
        message = "They are out."

    if query in ["add_markus", "jemimas_new_number", "mauriseu_guys_leaving"]:
        key_order = COLUMN_ORDERS["all_appl"]
    else:
        key_order = COLUMN_ORDERS[query]

    return render_template("list.html",
                           result=result,
                           key_order=key_order,
                           key_aliases=ALIASES,
                           description=DESC[query],
                           message=message)


@app.route("/reset", methods=["GET"])
def reset():
    os.system("psql -f application_process_sample_data_2.sql")
    return redirect('/')


@app.route("/choose_table", methods=["GET"])
def select_table():
    return render_template("form.html")


@app.route("/list_table", methods=["POST"])
def show_table_page():
    table_name = request.form
    if table_name["table"] == "1":
        table_name = "applicants"
        order = "all_appl"
    elif table_name["table"] == "2":
        table_name = "mentors"
        order = "all_ment"
    elif table_name["table"] == "3":
        table_name = "schools"
        order = "all_schools"
    elif table_name["table"] == "4":
        table_name = "applicants_mentors"
        order = "all_app_ment"

    result = queries.show_table(table_name)
    return render_template("list.html",
                           result=result,
                           key_order=COLUMN_ORDERS[order],
                           key_aliases=ALIASES,
                           )


def add_markus():
    result = queries.get_markus_info()
    if not result:
        queries.get_markus_into_the_system("Do not fetch")
        result = queries.get_markus_info()
    return result


if __name__ == "__main__":
    app.run(debug=True)
