import numpy
import pandas

'''
https://classroom.udacity.com/courses/ud359/lessons/735339002/concepts/7029292570923
You are given a list of Titantic passengers and their information. Here's the algorithm, predict the passenger survived if:
1) If the passenger is female or
2) if his/her socioeconomic status is high AND if the passenger is under 18

Write your prediction back into the "predictions" dictionary. The
key of the dictionary should be the Passenger's id and the associated value should be 1 if the passenger survived or 0 otherwise.
'''

predvidjanja = {}
putnici = pandas.read_csv('../podaci/titanic_data.csv')

for index, putnik in putnici.iterrows():
    id = putnik['PassengerId']
    predvidjanja[id] = (
        (putnik['Sex'] == 'female') or
        (putnik['Age'] < 18 and putnik['Pclass'] == 1)
    )

print predvidjanja

#  na osnovu ovih kriterija, predvidjanje smrtnosti se poklapa 79.12% sa statistikama
