import pandas as pd

series = pd.Series(
    ['Dave', 'Cheng-Han', 359, 9001], index=['Instructor', 'Curriculum Manager', 'Course Number', 'Power Level'])

print series
print "Instruktor je " + series['Instructor']
