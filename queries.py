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
    query = """SELECT COALESCE(mentors.first_name, 'No data') AS first_name,
                      COALESCE(mentors.last_name, 'No data') AS last_name,
                      schools.name, schools.country
               FROM mentors RIGHT JOIN schools
               ON (mentors.city = schools.city)
               ORDER BY mentors.id;"""
    return query


@connection_handler
def mentors_by_country():
    query = """SELECT schools.country, COUNT(mentors.id) AS count
               FROM mentors JOIN schools
               ON (mentors.city = schools.city)
               GROUP BY schools.country
               ORDER BY schools.country;"""
    return query


@connection_handler
def school_contacts():
    query = """SELECT schools.name,
               COALESCE(mentors.first_name, 'No data') AS first_name,
               COALESCE(mentors.last_name, 'No data') AS last_name
               FROM mentors RIGHT JOIN schools
               ON (mentors.id = schools.contact_person)
               ORDER BY schools.name;"""
    return query


@connection_handler
def applicants_after_2016():
    query = """SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
               FROM applicants JOIN applicants_mentors
               ON (applicants.id = applicants_mentors.applicant_id)
               WHERE applicants_mentors.creation_date > '2016-01-01'
               ORDER BY applicants_mentors.creation_date DESC;"""
    return query


@connection_handler
def applicants_and_mentors():
    query = """SELECT applicants.first_name AS applicant, applicants.application_code,
               COALESCE(mentors.first_name, 'No data') AS first_name,
               COALESCE(mentors.last_name, 'No data') AS last_name
               FROM applicants
               LEFT JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
               LEFT JOIN mentors ON mentors.id = applicants_mentors.mentor_id
               ORDER BY applicants.id;"""
    return query


######################################
#       Queries from previous SI     #
######################################


@connection_handler
def get_mentors_full_name():
    query = """SELECT first_name, last_name
               FROM mentors;"""
    return query


@connection_handler
def get_mentor_nicks_from_miskolc():
    query = """SELECT nick_name
               FROM mentors WHERE city = 'Miskolc';"""
    return query


@connection_handler
def get_me_carols_number():
    query = """SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
               FROM applicants
               WHERE first_name = 'Carol';"""
    return query


@connection_handler
def carol_dumped_me_give_me_any_other_girls_number():
    query = """SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
               FROM applicants
               WHERE email LIKE '%@adipiscingenimmi.edu';"""
    return query


@connection_handler
def get_markus_info():
    query = """SELECT *
              FROM applicants
              WHERE application_code = 54823;"""
    return query


@connection_handler
def get_markus_into_the_system(*args):
    query = """INSERT INTO applicants(first_name, last_name, phone_number, email, application_code)
              VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);"""
    return query


@connection_handler
def update_jemimas_number():
    query = """UPDATE applicants
               SET phone_number = '003670/223-7459'
               WHERE first_name = 'Jemima' AND last_name = 'Foreman';
               SELECT *
               FROM applicants
               WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""
    return query


@connection_handler
def get_mauriseu_guys_id():
    query = """SELECT id FROM applicants
               WHERE email LIKE '%@mauriseu.net';"""
    return query


@connection_handler
def kick_that_mauriseu_guys_out_updated(*args):
    mauriseu_ids = get_mauriseu_guys_id()
    query = ""
    for i in mauriseu_ids:
        query += "DELETE FROM applicants_mentors WHERE applicant_id = " + str(i["id"]) + "; "
        query += "DELETE FROM applicants WHERE id = " + str(i["id"]) + "; "
    return query

######################################
#           Extra features           #
######################################
