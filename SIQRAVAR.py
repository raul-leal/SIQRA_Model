import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N = 100
S0 = 30
I0 = 5
Q0 = 0
R0 = 5
A0 = 60

# Select what parameter to study
parameter = str(input('Escolha qual parâmetro variar (escreva igual está no código): '))

fig = plt.figure(facecolor="w")
ax = fig.add_subplot(111, facecolor = 'w', axisbelow = True)
ax.set_title(f'Parâmetro variado = {parameter}')
ax.set_xlabel('Time')
ax.set_xlim(0, 10)
ax.set_ylabel('Population')
ax.set_ylim(0, 100)
legend = ax.legend()
legend.get_frame().set_alpha(0.5)


if parameter == 'beta' or parameter == 'alfa' or parameter == 'sigma' or parameter == 'alfaIA' or parameter == 'alfaQA':
    variation = np.arange(0.1, 1.1, 0.1)
elif parameter == 'delta' or parameter == 'omega':
    variation = np.arange(1.0, 11, 1.0)
elif parameter == 'alfaSA':
    variation = np.arange(0.001, 0.101, 0.01)
else: variation = 0


for i in variation:
    if parameter == 'beta':
        beta = round(i,2)
    else: beta = 0.1
    if parameter == 'delta':
        delta = round(i,2)
    else: delta = 9
    if parameter == 'alfa':
        alfa = round(i,2)
    else: alfa = 0.5
    if parameter == 'sigma':
        sigma = round(i, 2)
    else: sigma = 0.8
    if parameter == 'omega':
        omega = round(i,2)
    else: omega = 2
    if parameter == 'alfaSA':
        alfaSA = round(i,2)
    else: alfaSA = 0.025
    if parameter == 'alfaIA':
        alfaIA = round(i,3)
    else: alfaIA = 0.25
    if parameter == 'alfaQA':
        alfaQA = round(i,2)
    else: alfaQA = 0.5
    
            

    # A grid of time points
    t = np.linspace(0, 10)

    # The SIQRA model differential equations
    def SIQRA(y, t, N, beta, delta, alfa, sigma, omega, 
            alfaSA, alfaIA, alfaQA):
        S, I, Q, R, A = y
        dSdt = -alfaSA * S * A - beta * S * I + sigma * R + omega * Q
        dIdt = beta * S * I - alfaIA * A * I - delta * I
        dQdt = delta * I - omega * Q - alfaQA * Q - alfa * Q
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
    ax.plot(t, S, label='Susceptible')
    ax.plot(t, I, '--', label='Infected')
    ax.plot(t, Q, '.-', label='Quarantine')
    ax.plot(t, R, '*', label='Removed')
    ax.plot(t, A, 'o', label='Antidotal')

plt.show()