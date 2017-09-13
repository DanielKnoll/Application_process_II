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
    query = """SELECT a.first_name AS applicant, a.application_code, m.first_name, m.last_name
               FROM applicants a, applicants_mentors am, mentors m
               WHERE a.id = am.applicant_id AND m.id = am.mentor_id
               ORDER BY a.id;"""
    return query
