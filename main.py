from scf import GaussianChain

if __name__ == "__main__":
    gs = GaussianChain(lattice="cubic")
    print(gs.force(0.5))
    print(gs.stretching(0.5))
