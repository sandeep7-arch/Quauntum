import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def time(hour, minutes):
    hour_angle = 2 * np.pi * (((hour % 12) / 12) + (minutes / 720))
    minute_angle = 2 * np.pi * (minutes / 60)

    qml.RY(hour_angle, wires=0)
    qml.RY(minute_angle, wires=1)

    return qml.probs(wires=[0, 1])

h = int(input("Enter Hour's hand time position : "))
m = int(input("Enter Minute's hand time position : "))
probs = time(h, m)
print(probs)
