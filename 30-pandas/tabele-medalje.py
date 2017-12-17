from pandas import DataFrame, Series
import numpy as np
import json

medalje = json.load(open('../podaci/medalje-sochi-2014.json'))
medalje_df = DataFrame(medalje)

print medalje_df

# stampa odredjenu kolonu
print medalje_df['country_name']

# stampa vise kolona
print medalje_df[['country_name', 'gold']]

# stampa samo osvajace zlata
print medalje_df[medalje_df['gold'] > 0]

# stampa prosek medalja po zemlji
prosek_medalja = medalje_df[['gold', 'silver', 'bronze']].apply(np.mean)
print prosek_medalja

# racuna poene za svaku zemlju po kljucu zlato:4, srebro:2, bronza:1
broj_medalja = medalje_df[['gold', 'silver', 'bronze']]
poeni = np.dot(broj_medalja, [4, 2, 1])

poeni_po_drzavi = DataFrame({
    'country_name': medalje['country_name'],
    'poeni': poeni
})

print poeni_po_drzavi
