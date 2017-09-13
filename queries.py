from database_common import connection_handler


@connection_handler
def mentors_and_schools():
    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
               FROM mentors JOIN schools
               ON (mentors.city = schools.city)
               ORDER BY mentors.id;"""
    return query


@connection_handler
def all_schools():
    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
               FROM mentors RIGHT JOIN schools
               ON (mentors.city = schools.city)
               ORDER BY mentors.id;"""
    values = ""
    return query
