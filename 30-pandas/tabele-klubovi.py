import pandas as pd

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data)

print "stampa celu tabelu"
print football

print "stampa samo prvi red"
print football.loc[[0]]

print "stampa od 3 do 6 reda"
print football[3:6]

print "stampa klubove sa deset i vise pobeda"
print football[football.wins > 10]
# print football[(football.wins > 10) & (football.team == "Packers")]
