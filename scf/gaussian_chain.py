from typing import Literal

import numpy as np


class GaussianChain:
    def __init__(self, lattice: Literal["linear", "cubic", "continual", "hexagonal"]):
        self.lattice = lattice

    def stretching(self, force: float) -> float:
        if self.lattice == "linear":
            return force / 3
        elif self.lattice == "cubic":
            return np.sinh(force) / (np.cosh(force) + 2)
        elif self.lattice == "continual":
            if force <= 0.0:
                raise ValueError("force must be more than 0")
            return np.cosh(force) / np.sinh(force) - 1 / force
        elif self.lattice == "hexagonal":
            # TODO
            return 0.0
        else:
            raise TimeoutError("unkonown lattice type")

    def force(self, r: float) -> float:
        """_summary_

        Args:
            r (float): relative stretching, H/N

        Raises:
            TimeoutError: unkonown lattice type

        Returns:
            float: force
        """
        if r < 0 or r > 1:
            raise ValueError("r must be (0, 1)")
        if self.lattice == "linear":
            return 3 * r
        elif self.lattice == "cubic":
            return np.log((2 * r + np.sqrt(1 + r**2)) / (1 - r))
        elif self.lattice == "continual":
            # TODO
            return 0.0
        elif self.lattice == "hexagonal":
            # TODO
            return 0.0
        else:
            raise TimeoutError("unkonown lattice type")
        return 0.0
