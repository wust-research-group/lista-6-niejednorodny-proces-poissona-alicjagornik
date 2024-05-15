import numpy as np
import math

def generate_waiting_times(intensity_function, T):
    times = []
    t = 0
    counter = 0
    while t < T:
        u = np.random.uniform()
        t += -np.log(u) / intensity_function(t)
        if t < T:
            times.append(t)
            counter += 1
    return times, counter

def intensity_function(t):
    return 0.5 * np.sin(t) + 0.3

waiting_times, counter = generate_waiting_times(intensity_function, 100)
print(waiting_times)

#Sprawdzenie
ch = []
k = counter
for time in waiting_times:
    lam = 0.3 * time - 0.5 * np.cos(time) + 0.5
    n = np.exp(-lam) * lam**k / math.factorial(k)
    ch.append(n)

print(ch)