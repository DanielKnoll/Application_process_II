COLUMN_ORDERS = {"mentors": ["first_name", "last_name", "name", "country"],
                 "all_schools": ["first_name", "last_name", "name", "country"],
                 "mentors_by_country": ["country", "count"],
                 "contacts": ["name", "first_name", "last_name"],
                 "applicants": ["first_name", "application_code", "creation_date"],
                 "applicants_and_mentors": ["applicant", "application_code", "first_name", "last_name"]}

ALIASES = {"first_name": "First name",
           "last_name": "Last name",
           "name": "School name",
           "country": "Country",
           "count": "Number of mentors",
           "application_code": "Applicant's code",
           "creation_date": "Creation date"}
