import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N = 100
S0 = 98
I0 = 1
Q0 = 0
R0 = 0
A0 = 1

'''
# Total population, N
N = int(input("Total number of the population: "))
# Initial number of S, I, Q, R and A nodes
I0 = int(input("Initial number of infected nodes: "))
R0 = 5
Q0 = 0
A0 = 1
S0 = N - I0 - R0 - Q0 - A0 # Everyone else is susceptible
# Contact rate between nodes

beta = float(input("Rate between S and I, beta: "))
delta = float(input("Rate between I and Q, delta: "))
alfa = float(input("Rate between Q and A, alfa: "))
sigma = float(input("Rate between R and S, sigma: "))
omega = float(input("Rate between Q and S, omega: "))
alfaSA = float(input("Rate between S and A, alfaSA: "))
alfaIA = float(input("Rate between I and A, alfaIA: "))
alfaQA = float(input("Rate between Q and A, alfaQA: "))
'''

beta = 0.1
delta = 9
alfa = 0.5
sigma = 0.8
omega = 2
alfaSA = 0.025
alfaIA = 0.25
alfaQA = 0.5

# A grid of time points
t = np.linspace(0, 10)

# The SIQRA model differential equations with nonlinear IQ term
def SIQRA(y, t, N, beta, delta, alfa, sigma, omega, 
          alfaSA, alfaIA, alfaQA):
    S, I, Q, R, A = y
    dSdt = -alfaSA * S * A - beta * S * I + sigma * R + omega * Q
    dIdt = beta * S * I - alfaIA * A * I - delta * Q * I
    dQdt = delta * Q * I - omega * Q - alfaQA * Q - alfa * Q
    dRdt = alfa * Q - sigma * R
    dAdt = alfaSA * S * A + alfaIA * A * I + alfaQA * Q
    return dSdt, dIdt, dQdt, dRdt, dAdt

# Initial conditions vector
y0 = S0, I0, Q0, R0, A0
# Integrate the SIQRA equations over the time grid, t
ret = odeint(SIQRA, y0, t, args=(N, beta,  delta, alfa,
                                  sigma, omega, alfaSA, alfaIA, alfaQA))
S, I, Q, R, A = ret.T

# Plot the data on five different curves for S(t), I(t), Q(t), R(t), A(t)
fig = plt.figure(facecolor="w")
ax = fig.add_subplot(111, facecolor='w', axisbelow = True)
ax.plot(t, S, label='Susceptible')
ax.plot(t, I, '--', label='Infected')
ax.plot(t, Q, '.-', label='Quarantine')
ax.plot(t, R, '*', label='Removed')
ax.plot(t, A, 'o', label='Antidotal')
ax.set_xlabel('Time')
ax.set_xlim(0, 10)
ax.set_ylabel('Population')
ax.set_ylim(0, 100)
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
plt.show()