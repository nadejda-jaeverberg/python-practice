def print_matrix(matrix):
    out_str = ""
    for l in matrix:
        row_str = ""
        for jj in l:
            row_str = row_str + f"\t{jj}"
        out_str = out_str + "\n" + row_str
    return out_str + "\n"


def flipping_matrix(matrix):
    mstr = print_matrix(matrix)
    print(mstr)
    n = len(matrix)
    maxs = []
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            print(f"Buddies for element: {i}, {j} are \t{n-i-1}, {n-j-1}\t{i}, {n-j-1}\t{n-i-1}, {j}")
            m1 = [matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1]]
            maxs.append(max(m1))
    return sum(maxs)
