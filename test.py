import numpy as np
from numpy.linalg import inv

if __name__ == '__main__':

    # Init Matrix
    # Columns are lines
    A = np.array([
        [1., 2.],
        [3., 4.]
    ])

    # Swap lines 1 and 2
    P = np.array([
        [0., 1.],
        [1., 0.]
    ])
    print("A x P")
    print(A.dot(P))

    # Invert matrix
    print("\n A inverted")
    print(inv(A))
