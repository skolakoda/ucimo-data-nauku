from pandas import DataFrame, Series
import numpy as np
import json

medalje = DataFrame(json.load(open('../podaci/medalje-sochi-2014.json')))

broj_medalja = medalje[['gold', 'silver', 'bronze']]
prosek_medalja = broj_medalja.apply(np.mean) # prosek
print "Prosek medalja po zemlji:"
print prosek_medalja

poeni = np.dot(broj_medalja, [4, 2, 1]) # dot product
poeni_po_drzavi = DataFrame({
    'country_name': medalje['country_name'],
    'poeni': poeni
})
print "Poeni zemalja po kljucu zlato:4, srebro:2, bronza:1"
print poeni_po_drzavi
