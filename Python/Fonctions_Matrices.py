import numpy
import numpy as np

if __name__ == '__main__':

    A = np.array([
        [3., 2.],
        [1., 4.]
    ])

    B = np.array([
        [2., 1.],
        [1., 1.]
    ])

    print("\nA + B")
    print(A + B)

    print("\nA x B")
    print(A.dot(B))
    C = np.array([
        [2., 3., 0.],
        [1., 4., 5.],
        [7., 2., 1.]
    ])
    print("\nDeterminant")
    print(np.linalg.det(C))

    print('\nResolution Ax = B')
    A = np.array([
        [1, 1, 1, 1],
        [0, 3, 3, 3],
        [0, 0, 2, 1],
        [0, 0, 1, 1]
    ])

    b = [205, 300, 120, 90]
    x = np.linalg.solve(A, b)
    print(x)

    print('\nInverse')
    A = np.array([
        [2, 3],
        [4, 2]
    ])

    B = np.linalg.inv(A)
    print(B)