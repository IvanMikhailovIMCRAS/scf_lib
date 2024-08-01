import matplotlib.pyplot as plt
import numpy as np

from scf import GaussianChain, Lattice

if __name__ == "__main__":

    F = []
    D = []

    N = 16
    for n_layers in range(1, N):

        Gf = np.zeros(shape=(n_layers + 2, N))
        Gb = np.zeros(shape=(n_layers + 2, N))

        Gf[1, 0] = 1
        Gb[n_layers, N - 1] = 1
        lam_b = 1 / 6
        lam_f = 1 / 6
        lam_0 = 1 - lam_b - lam_f

        for s in range(1, N):
            for z in range(1, n_layers + 1):
                Gf[z, s] = (
                    lam_b * Gf[z - 1, s - 1]
                    + lam_0 * Gf[z, s - 1]
                    + lam_f * Gf[z + 1, s - 1]
                )

        for s in range(N - 2, -1, -1):
            for z in range(1, n_layers + 1):
                Gb[z, s] = (
                    lam_f * Gb[z - 1, s + 1]
                    + lam_0 * Gb[z, s + 1]
                    + lam_b * Gb[z + 1, s + 1]
                )

        Q = np.sum(Gf * Gb) / N
        F.append(-np.log(Q))
        D.append(n_layers - 1)

F = np.array(F)
D = np.array(D)

Gs = GaussianChain(lattice="cubic")

force = np.diff(F) / np.diff(D)
plt.plot((D[:-1] + D[1:]) * 0.5, force)
plt.plot(D[1:], [Gs.force(d / N) for d in D[1:]])
plt.ylim(0, np.max(force))
plt.show()
