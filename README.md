# Shrodinger_Probability

This project simulates a quantum particle confined in a one-dimensional potential well, computing the stationary wavefunctions and their probability distributions $∣ψ(x)^2|$. The code, assuming m = ℏ = 1 for simplicity, numerically solves the time-independent Schrödinger equation by approximating $\frac{d^2ψ}{dx^2}≈\frac{ψ(x+Δx)−2ψ(x)+ψ(x-Δx)}{Δx^2}$. This leads to a Hamiltonian matrix representation that is a sum of the matrices representing both kinetic and potential energy, while keeping in mind ψ = 0 at the domain edges. Once the Hamiltonian is complete, the simulation uses eigenvalue solvers to find its eigenvalues and eigenvectors. Finally, the code plots the probability density across the 1D domain of the specified states.

Prerequisites: Ensure you have Python 3 installed, along with the required libraries. You can obtain the code by cloning the project repository or downloading the Python source file. If using a Jupyter Notebook, simply run the notebook cells in order. If using a Python script, run it from the command line or an IDE. To install the dependencies run:
``` pip install numpy scipy matplotlib ```
