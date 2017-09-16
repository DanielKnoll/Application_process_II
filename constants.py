COLUMN_ORDERS = {
    "mentors": ["first_name", "last_name", "name", "country"],
    "all_school": ["first_name", "last_name", "name", "country"],
    "mentors_by_country": ["country", "count"],
    "contacts": ["name", "first_name", "last_name"],
    "applicants": ["first_name", "application_code", "creation_date"],
    "applicants_and_mentors": ["applicant", "application_code", "first_name", "last_name"],
    "mentors_full_name": ["first_name", "last_name"],
    "mentors_nick_from_miskolc": ["nick_name"],
    "carols_number": ["full_name", "phone_number"],
    "hat_owner": ["full_name", "phone_number"],
    "all_appl": ["id", "first_name", "last_name", "phone_number", "email", "application_code"],
    "all_ment": ["id", "first_name", "last_name", "nick_name", "phone_number", "email", "city", "favourite_number"],
    "all_schools": ["id", "name", "city", "country", "contact_person"],
    "all_app_ment": ["applicant_id", "mentor_id", "creation_date"]
    }

ALIASES = {"first_name": "First name",
           "last_name": "Last name",
           "name": "School name",
           "country": "Country",
           "count": "Number of mentors",
           "applicant": "Applicant",
           "application_code": "Applicant's code",
           "creation_date": "Creation date",
           "nick_name": "Nick name",
           "full_name": "Full name",
           "phone_number": "Phone number",
           "email": "Email",
           "id": "ID",
           "city": "City",
           "favourite_number": "Fav number",
           "contact_person": "Contact person",
           "applicant_id": "Applicant ID",
           "mentor_id": "Mentor ID",
           "creation_date": "Creation date"}

DESC = {"mentors": """1. Mentors and schools page [/mentors]
                      On this page you should show the result of a query that returns the name of the
                      mentors plus the name and country of the school (joining with the schools table)
                      ordered by the mentors id column (columns: mentors.first_name, mentors.last_name,
                      schools.name, schools.country). """,
        "all_school": """2. All school page [/all-school]
                         On this page you should show the result of a query that returns the name of the
                         mentors plus the name and country of the school (joining with the schools table)
                         ordered by the mentors id column. BUT include all the schools, even if there's
                         no mentor yet (in that cell, "No data" should be displayed)! columns:
                         mentors.first_name, mentors.last_name, schools.name, schools.country""",
        "mentors_by_country": """3. Mentors by country page [/mentors-by-country]
                                 On this page you should show the result of a query that returns the number
                                 of the mentors per country ordered by the name of the countries columns:
                                 country, count""",
        "contacts": """4. Contacts page [/contacts]
                       On this page you should show the result of a query that returns the name of the
                       school plus the name of contact person at the school (from the mentors table)
                       ordered by the name of the school. columns: schools.name, mentors.first_name,
                       mentors.last_name""",
        "applicants": """5. Applicants page [/applicants]
                         On this page you should show the result of a query that returns the first name and
                         the code of the applicants plus the creation_date of the application (joining with
                         the applicants_mentors table) ordered by the creation_date in descending order BUT
                         only for applications later than 2016-01-01 columns: applicants.first_name,
                         applicants.application_code, applicants_mentors.creation_date""",
        "applicants_and_mentors": """6. Applicants and mentors page [/applicants-and-mentors]
                                     On this page you should show the result of a query that returns the
                                     first name and the code of the applicants plus the name of the assigned
                                     mentor (joining through the applicants_mentors table) ordered by the
                                     applicants id column Show all the applicants, even if they have no
                                     assigned mentor in the database! In this case use the string "No data"
                                     instead of the mentor name. columns: applicants.first_name,
                                     applicants.application_code, mentors.first_name, mentors.last_name""",
        "mentors_full_name":  """1. Write a query that returns the 2 name columns of the mentors table.
                                 columns: first_name, last_name""",
        "mentors_nick_from_miskolc": """2 .Write a query that returns the nick_name-s of all mentors
                                        working at Miskolc. column: nick_name""",
        "carols_number": """3. We had interview with an applicant, some Carol. We don't remember her name,
                            but she left her hat at the school. We want to call her to give her back her
                            hat. To look professional, we also need her full name when she answers the
                            phone (for her full_name, you want to include a concatenation into your query,
                            to get her full_name, like: "Carol Something" instead of having her name in 2
                            different columns in the result. This columns should be called: full_name).
                            columns: full_name, phone_number""",
        "hat_owner": """4. We called Carol, and she said it's not her hat. It belongs to another girl, who
                        went to the famous Adipiscingenimmi University. You should write a query to get
                        the same informations like with Carol, but for this other girl. The only thing
                        we know about her is her school e-mail address ending: '@adipiscingenimmi.edu'.
                        columns: full_name, phone_number""",
        "add_markus": """5. After we returned the hat, a new applicant appeared at the school, and he wants
                         to get into the application process. His name is Markus Schaffarzyk, has a number:
                         003620/725-2666 and e-mail address: djnovus@groovecoverage.com Our generator gave
                         him the following application code: 54823. After INSERTing the data, write a SELECT
                         query, that returns with all the columns of this applicant! (use the unique
                         application code for your condition!)""",
        "jemimas_new_number": """6. Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
                                 Write an UPDATE query, that changes this data in the database for this applicant.
                                 Also, write a SELECT query, that checks the phone_number column of this applicant.
                                 Use both of her name parts in the conditions!""",
        "mauriseu_guys_leaving": """7. Arsenio, an applicant called us, that he and his friend applied to Codecool.
                                    They both want to cancel the process, because they got an investor for the site
                                    they run: mauriseu.net Write DELETE query to remove all the applicants, who
                                    applied with emails for this domain (e-mail address has this domain after
                                    the @ sign).""",
        }
