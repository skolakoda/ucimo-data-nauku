import numpy
import scipy.stats
import pandas

# poredjenje levorukih i desnorukih igraca
podaci = pandas.read_csv('../podaci/baseball_stats.csv')
levoruki = podaci[podaci['handedness'] == 'L']
desnoruki = podaci[podaci['handedness'] == 'R']

# t-test
rezultat = scipy.stats.ttest_ind(levoruki['avg'], desnoruki['avg'], equal_var=False)

print "Da li levoruki imaju znacajno razlicite rezultate od desnorukih?"
print (rezultat[1] > 0.5, rezultat)
