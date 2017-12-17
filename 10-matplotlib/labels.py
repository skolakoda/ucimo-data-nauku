import matplotlib.pyplot as plt
year = [1950, 1951, 1952, 2100]
pop = [2.538, 2.57, 2.62, 10.85]

plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')

plt.show()
