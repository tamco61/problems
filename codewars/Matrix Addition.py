def matrix_addition(a, b):
    c = [[0 for i in range(len(r))] for r in a]
    for r in range(len(a)):
        for i in range(len(a[r])):
            c[r][i] = b[r][i] + a[r][i]
    return c