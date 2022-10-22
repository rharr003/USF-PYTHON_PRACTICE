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
    result = 0
    for n in matrix:
        result += n[matrix.index(n)]
        result += n[(len(n) -1) - matrix.index(n)]
    return result


m2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
         ]
print(sum_up_diagonals(m2))