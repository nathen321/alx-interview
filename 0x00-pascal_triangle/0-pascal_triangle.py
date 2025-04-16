def pascal_triangle(n):
    if (n <= 0):
        return []
    tri = [[1]]
    while (n > 1):
        row = []
        for i in range(len(tri[-1])):
            if i == 0:
                row.append(1)
            else:
                row.append(tri[-1][i - 1] + tri[-1][i])
        row.append(1)
        tri.append(row)
        n -= 1
    return tri
