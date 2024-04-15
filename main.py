from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt
from time import time

# daten einladen
data = load_data('activity.csv')
power_W = data['PowerOriginal']
print ("power p ist",power_W)
# daten sortieren
sorted_power_W = bubble_sort(power_W)
print("das ist sortierte Power",sorted_power_W[::-1])
# daten plotten

plt.plot(sorted_power_W[::-1])
plt.xlabel("Dauer in Sekunden")
plt.ylabel("Leistung in W")
plt.grid(True)
plt.savefig("Leistungskurve.png")
plt.show()
