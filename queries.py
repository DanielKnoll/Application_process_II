import database_common


@database_common.connection_handler
def get_mentor_names():
    first_name = "László"
    quary = """SELECT * FROM mentors
               WHERE first_name = %(f_n)s ORDER BY first_name;"""
    values = {'f_n': first_name}
    return quary, values
