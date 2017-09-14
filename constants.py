COLUMN_ORDERS = {"mentors": ["first_name", "last_name", "name", "country"],
                 "all_school": ["first_name", "last_name", "name", "country"],
                 "mentors_by_country": ["country", "count"],
                 "contacts": ["name", "first_name", "last_name"],
                 "applicants": ["first_name", "application_code", "creation_date"],
                 "applicants_and_mentors": ["applicant", "application_code", "first_name", "last_name"],
                 "mentors_full_name": ["first_name", "last_name"],
                 "mentors_nick_from_miskolc": ["nick_name"],
                 "carols_number": ["full_name", "phone_number"],
                 "hat_owner": ["full_name", "phone_number"],
                 "all_appl": ["id", "first_name", "last_name", "phone_number", "email", "application_code"]
                 }

ALIASES = {"first_name": "First name",
           "last_name": "Last name",
           "name": "School name",
           "country": "Country",
           "count": "Number of mentors",
           "application_code": "Applicant's code",
           "creation_date": "Creation date",
           "nick_name": "Nick name",
           "full_name": "Full name",
           "phone_number": "Phone number",
           "email": "Email"}
