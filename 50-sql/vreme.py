import pandas
import pandasql

weather_data = pandas.read_csv('../podaci/weather-underground.csv')

# SQL query should return one column and one row - a count of the number of days in the dataframe where the rain column is equal to 1 (days it rained)

q = """
SELECT COUNT(*)
FROM weather_data
WHERE rain = 1
"""

rainy_days = pandasql.sqldf(q.lower(), locals())
print rainy_days
