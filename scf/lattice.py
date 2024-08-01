from typing import Literal

import numpy as np


class Lattice:
    def __init__(
        self,
        geometry: Literal["flat", "cyllindrical", "spherical"],
        n_layers: int,
        r_ofset: float = 0.0,
    ):
        self.geometry = geometry
        self.n_layers = n_layers
        self.r_ofset = r_ofset

        lam_f = np.zeros(n_layers, dtype=float)
        lam_b = np.zeros(n_layers, dtype=float)
        lam_0 = np.zeros(n_layers, dtype=float)

        r = np.arange(n_layers) + r_ofset

        if geometry == "flat":

            lam_f[:] = 1 / 6
            lam_b[:] = 1 / 6

        elif geometry == "cyllindrical":

            lam_f[:] = 1 / 6 * (2 * r[:] + 1) / (2 * (r[:] + 1))
            lam_b[:] = 1 / 6 * (2 * r[:] + 1) / (2 * r[:])

        elif geometry == "spherical":

            lam_f[:] = 1 / 6 * 1 / 3 * ((r[:] + 1) ** 3 + r[:] ** 3) / ((r[:] + 1) ** 2)
            lam_b[:] = 1 / 6 * 1 / 3 * ((r[:] + 1) ** 3 - r[:] ** 3) / (r[:] ** 2)

        lam_0[:] = 1.0 - lam_f[:] - lam_b[:]
