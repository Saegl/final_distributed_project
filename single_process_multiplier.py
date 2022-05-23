from random import randint
import time

X = []
Y = []
Z = []

N = 500


def init_matrix():
    global X
    X = [[randint(0, 9) for i in range(N)] for j in range(N)]

    global Y
    Y = [[randint(0, 9) for i in range(N)] for j in range(N)]


def multiply_matrix(X, Y):
    global Z
    Z = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)]
            for X_row in X]


def multiply():
    Z = [[0] * len(Y[0]) for i in range(len(X))]

    i = 0
    for a in X:
        j = 0
        for b in a:
            k = 0
            for c in Y[j]:
                Z[i][k] = Z[i][k] + (b * c)
                k = k + 1
            j = j + 1
        i = i + 1


if __name__ == '__main__':
    init_matrix()

    # start time
    t1 = time.time()
    print('Start time', t1)

    multiply_matrix(X, Y)

    # end time
    t2 = time.time()
    print('End time', t2)
    print("Time taken in milliseconds", int((t2 - t1) * 1000))
