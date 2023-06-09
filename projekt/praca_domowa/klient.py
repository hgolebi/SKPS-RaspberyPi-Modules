import socket
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter

HOST = "127.0.0.1"
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


def receive_data(socket):
    return (socket.recv(64).decode("utf-8")).replace('\x00', '')


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, s), interval=1000)
        plt.show()

if __name__ == "__main__":
    main()
