import pandas
import pandasql

# normalize columns by replacing spaces with underscores and characters to lowercase
aadhaar_data = pandas.read_csv('../podaci/aadhaar_data.csv')
aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

q = """
SELECT gender, district, sum(aadhaar_generated)
FROM aadhaar_data
WHERE age > 50
GROUP BY gender, district;
"""

aadhaar_solution = pandasql.sqldf(q.lower(), locals())
print aadhaar_solution
