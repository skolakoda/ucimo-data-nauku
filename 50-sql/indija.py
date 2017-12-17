import pandas
import pandasql

# normalize columns by replacing spaces with underscores and characters to lowercase
aadhaar_data = pandas.read_csv('../podaci/aadhaar_data.csv')
aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

# Select first 50 values for "registrar" and "enrolment_agency" using SQL syntax
q = """
SELECT registrar, enrolment_agency
from aadhaar_data
limit 50
"""

aadhaar_solution = pandasql.sqldf(q.lower(), locals())
print aadhaar_solution
