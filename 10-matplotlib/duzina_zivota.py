# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # naša slova

import matplotlib.pyplot as plt
import json

gdp_cap = json.load(open('../podaci/gdp_cap.json'))
life_exp = json.load(open('../podaci/life_exp.json'))
population = json.load(open('../podaci/population.json'))

plt.scatter(gdp_cap, life_exp, s=population)
plt.xscale('log')

plt.xlabel('BDP po glavi stanovnika [$]')
plt.ylabel('Očekivani životni vek')
plt.title('Bogatstvo i dužina života (podaci iz 2007)')

# dodaje natpise na x osi
plt.xticks([1000, 10000, 100000], ['1 hilj', '10 hilj', '100 hilj'])
# dodaje natpise na balonima
plt.text(1550, 71, 'Indija')
plt.text(5700, 80, 'Kina')

plt.show()
