import csv
from matplotlib import pyplot as plt
import numpy as np


filename = 'E:\PWR\Visual Studio\wstep_do_programowania\\rowery.csv'
stations = []
bikes_on_stations = {}
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        stations.append(str(row[2]))
        bikes_on_stations[str(row[2])] = stations.count(str(row[2]))

print(bikes_on_stations)
'''histogram:'''
plt.style.use('ggplot')
plt.hist(stations, bins=15, align='mid', label='liczba rowerow')
plt.title('Liczba rowerow na poszczegolnych stacjach rowerowch')
plt.xlabel('Numer stacji')
plt.ylabel('Liczba rowerow')
plt.legend(loc="upper right")
plt.show()


'''kolowy:'''
fig1, ax1 = plt.subplots()
ax1.pie(bikes_on_stations.values(), labels=bikes_on_stations.keys(), autopct='%1.1f%%',
        shadow=True, startangle=90,
        colors=("red", "green", "orange", "cyan", "brown", "grey", "blue"))
ax1.axis('equal')
plt.title('Liczba rowerow na poszczegolnych stacjach rowerowch')
plt.legend(loc="upper right")
plt.show()


'''liniowy:'''
plt.plot(bikes_on_stations.keys(), bikes_on_stations.values(),
         color='green', label='Liczba rowerow')
plt.title('Liczba rowerow na poszczegolnych stacjach rowerowch')
plt.xlabel('Numer stacji')
plt.ylabel('Liczba rowerow')
plt.grid(True)
plt.legend(loc="upper right")
plt.show()


'''rozrzutu:'''
area = np.pi*3
plt.scatter(bikes_on_stations.keys(), bikes_on_stations.values(), s=area,
            color="blue", edgecolors="white", linewidths=0.1,
            alpha=0.7, label='Liczba rowerow')
plt.title('Liczba rowerow na poszczegolnych stacjach rowerowch')
plt.xlabel('Numer stacji')
plt.ylabel('Liczba rowerow')
plt.legend(loc="upper right")
plt.show()