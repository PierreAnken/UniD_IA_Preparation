import numpy as np

from Python.integral_image.integral_image import IntegralImage

if __name__ == '__main__':

    base_matrix = np.array([
        [31., 2., 4., 33., 5., 36.],
        [12., 26., 9., 10., 29., 25.],
        [13., 17., 21., 22., 20., 18.],
        [24., 23., 15., 16., 14., 19.],
        [30., 8., 28., 27., 11., 7.],
        [1., 35., 34., 3., 32., 6.]
    ])

    summed_table = IntegralImage.get_summed_table(base_matrix)
    print('\nSummed table:')
    print(summed_table)

    print('\nSummed intensity:')
    intensity = IntegralImage.get_intensity(base_matrix, 2, 1, 2, 4, 4, 1, 4, 4)
    print(intensity)