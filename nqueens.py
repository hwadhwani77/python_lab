def totalNQueens(n):
    diag1 = set()
    diag2 = set()
    usedCols = set()
    return helper(n, diag1, diag2, usedCols, 0)
def helper(n, diag1, diag2, usedCols, row):
    if row == n:
        return 1
    s = 0
    for col in range(n):
        if row + col in diag1 or row - col in diag2 or col in usedCols:
            continue

        diag1.add(row + col)
        diag2.add(row - col)
        usedCols.add(col)

        s += helper(n, diag1, diag2, usedCols, row + 1)

        diag1.remove(row + col)
        diag2.remove(row - col)
        usedCols.remove(col)
    return s

print(totalNQueens(4))
