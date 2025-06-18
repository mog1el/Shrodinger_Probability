import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

a = float(input('Enter the lower limit: '))
b = float(input('Enter the upper limit: '))
N = int(input('Enter the N: '))

x = np.linspace(a,b,N)
h = x[1] - x[0]

Ekin = np.zeros((N-1, N-1))

for i in range(N-1):
    Ekin[i, i] = 2
    if i > 0:
        Ekin[i, i - 1] = -1
    if i < N - 2:
        Ekin[i, i + 1] = -1

Epot = np.zeros((N-1, N-1))

for i in range(N-1):
    Epot[i, i] = x[i+1]**2

H = (1/(2 * h**2)) * Ekin + Epot
e_vals, e_vecs = eigh(H)

for n in range(3):
    psi = e_vecs[:, n]
    P = psi**2
    P /= np.trapz(P, x[1:])
    plt.plot(x[1:], P)

plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.title('Wavefunctions')
plt.legend()
plt.grid(True)
plt.show()