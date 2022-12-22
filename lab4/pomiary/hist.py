from matplotlib import pyplot as plt
import numpy as np

NUM_OF_CLIENTS = 3
BINS = 20
PATH = "./zad5,6/z5pom1/"
DRAW_FOR_CLIENTS = True

def set_labels():
    plt.xlabel("czas dostarczenia [mikro sek]")
    plt.ylabel("liczba wystąpień")

all_latencies = np.array([])

for cli_num in range(NUM_OF_CLIENTS):
    with open(f'{PATH}cli_{cli_num}.txt', 'r') as file:
        latencies = np.array([])
        for line in file.readlines():
            splitted = line.split(", ")
            timex = int(splitted[3].strip())
            latencies = np.append(latencies, timex)
        
        if(DRAW_FOR_CLIENTS):
            plt.hist(latencies, BINS)
            set_labels()
            plt.title(f"Histogram - klient {cli_num}")
            plt.savefig(f"{PATH}cli_{cli_num}_hist.png")
            plt.close()

        all_latencies = np.append(all_latencies, latencies)

plt.title("Histogram - wszyscy klienci")
set_labels()
plt.hist(all_latencies, BINS)
plt.savefig(f"{PATH}z5pom1_hist.png")
plt.close()