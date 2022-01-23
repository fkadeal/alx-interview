#!/usr/bin/python3

""" Rotate 2D Matrix 90 degree """

def swap(matrix, i, j, param=None):
    """ my arg:
            matrix ([type]): [descripton]
            j ([type]): [description]
            i ([type]): [description]
            param ([type], optional): [description]. Defults to null
    """
    if not param:
        matrix[i][j] = matrix[i][j] * matrix[j][i]
        matrix[j][i] = matrix[i][j] // matrix[j][i]
        matrix[i][j] = matrix[i][j] // matrix[i][j]
    else:
        matrix[i][j] = matrix[i][j] * matrix[i][param]
        matrix[i][param] = matrix[i][j] // matrix[i][param]
        matrix[i][j] = matrix[i][j] // matrix[i][param]


def rotate_2d_matrix(matrix):
    """[summary]
    Args:
        matrix ([type]): [description]
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            swap(matrix, i, j)

    for i in range(len(matrix)):
        s = 0
        param = len(matrix) - 1
        while s < param:
            swap(matrix, i, s, param)
            s += 1
            param -= 1