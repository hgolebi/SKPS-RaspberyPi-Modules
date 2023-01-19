import socket
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter

HOST = "10.42.0.156"
PORT = 8080

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# function that is called every time interval 
# updates plot with received volatge value and timestamp of its receival
def animate(i, xs, ys, socket):

    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(float(receive_data(socket)))

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.yticks(np.arange(-2.50, 2.51, 0.5))
    plt.subplots_adjust(bottom=0.30)
    plt.title('Voltage over Time')
    plt.ylabel('Voltage (V)')
    plt.xlabel('Timestamp')

# receives data sent from RPi
def receive_data(socket):
    return socket.recv(8).decode("utf-8")


def main():
    # initializes socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # plots data on a constantly updated graph
        ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, s), interval=1)
        plt.show()

if __name__ == "__main__":
    main()
