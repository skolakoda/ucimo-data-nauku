import numpy as np

brojevi = [1, 2, 2, 3, 4, 5]

prosek = np.mean(brojevi) # aritmeticka sredina
medijan = np.median(brojevi) # centralna vrednost
devijacija = np.std(brojevi) # standardna devijacija (od proseka)

print ("Prosek", prosek)
print ("Medijan", medijan)
print ("Devijacija", devijacija)

# menja tipove niza
np_brojevi = np.array(brojevi)
np_decimali = np.array(brojevi, float)

print (brojevi)
print (np_brojevi)
print (np_decimali)
