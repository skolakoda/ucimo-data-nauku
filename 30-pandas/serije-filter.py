import pandas as pd

cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach',
                                             'Fish', 'Mini Pig', 'Puppy', 'Kitten'])

# stampa bul vrednost za svaki
print cuteness > 3
# stampa samo one koji zadovoljavaju
print cuteness[cuteness > 3]
