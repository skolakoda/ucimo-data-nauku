import numpy as np

two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)

print two_D_array
print two_D_array[1][1]
print two_D_array[1, :] # prvog niza svaki clan
print two_D_array[:, 2] # svakog niza treci index
