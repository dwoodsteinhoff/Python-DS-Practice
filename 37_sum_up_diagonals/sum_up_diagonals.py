m1 = [[1,   2],[30, 40]]
m2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
m3 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12],
      [13,14,15,16]]

def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    count = 0
    matrix_copy = matrix.copy()
    matrix_copy.reverse()

    for lst in matrix:
        for value in lst: 
            if lst.index(value) == matrix.index(lst):
                count += value

    for lst in matrix_copy:
        for value in lst:
            if lst.index(value) == matrix_copy.index(lst):
                count += value

    return count