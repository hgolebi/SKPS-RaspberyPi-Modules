from matplotlib import pyplot as plt
import numpy as np

NUM_OF_CLIENTS = 3
BINS = 20
PATH = "./zad5,6/z6pom/"

latencies = np.array([])

with open(f'{PATH}server.txt', 'r') as file:
    for line in file.readlines():
        splitted = line.split(", ")
        timex = int(splitted[2].strip())
        latencies = np.append(latencies, timex)

plt.title("Histogram")
plt.xlabel("czas między pobraniem próbek [mikro sek]")
plt.ylabel("liczba wystąpień")
plt.hist(latencies[1:], BINS)
axes = plt.gca()
print(axes.get_ylim())
plt.yticks(np.arange(0, round(axes.get_ylim()[1])+2, 2))
plt.savefig(f"{PATH}z6pom_server_hist.png")
plt.close()