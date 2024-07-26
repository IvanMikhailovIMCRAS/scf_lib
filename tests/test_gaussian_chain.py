from scf import GaussianChain

def test_force():
    gc = GaussianChain(lattice='linear')
    assert gc.force(0.5) == 3*0.5
    
def test_stretching():
    gc = GaussianChain(lattice='linear')
    assert gc.stretching(3) == 3/3
    