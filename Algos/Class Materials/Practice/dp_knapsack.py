def knapsackBU(w, plates: list):
    Matrix = []
    n = len(plates)
    for _ in range(n + 1):
        Matrix.append([0]*(w + 1))

    for ni in range(1, n + 1):
        for wj in range(1, w + 1):
            if plates[ni - 1] <= wj: 
                Matrix[ni][wj] = max(Matrix[ni - 1][wj - plates[ni - 1]]+ plates[ni - 1], Matrix[ni - 1][wj])
            else:
                Matrix[ni][wj] = Matrix[ni - 1][wj]
    return Matrix[n][w]


if __name__=='__main__':
    w, n = map(int, input().split())
    a = list(map(int, input().split()))
    print(knapsackBU(w, a))