import numpy as np


class IntegralImage:

    @staticmethod
    def get_summed_table(base_matrice):

        # check form and dimensions
        shape = base_matrice.shape
        if shape[0] != shape[1] or len(shape) != 2:
            raise ValueError('Base Matrix must be a 2d square matrix')

        size = shape[0]
        summed_table = np.zeros(shape)

        for line in range(0, size):
            for column in range(0, size):
                value = base_matrice[line][column]
                if line > 0:
                    value += summed_table[line-1][column]
                if column > 0:
                    value += summed_table[line][column - 1]
                if line > 0 and column > 0:
                    value -= summed_table[line-1][column-1]
                summed_table[line][column] = value

        return summed_table

    @staticmethod
    def get_intensity(base_table, ax, ay, bx, by, cx, cy, dx, dy):
        summed_table = IntegralImage.get_summed_table(base_table)
        size = summed_table.shape[0]

        for coordinate in [ax, ay, bx, by, cx, cy, dx, dy]:
            if coordinate < 0 or coordinate > size:
                raise ValueError('Invalid coordinate')
        a = summed_table[ax][ay]
        b = summed_table[bx][by]
        c = summed_table[cx][cy]
        d = summed_table[dx][dy]
        return d+a-b-c

