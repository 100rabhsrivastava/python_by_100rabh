rows = 6

for i in range(1, rows + 1):
    k= i-1
    for j in range(1, k):

        print(j, end="")

    for j in range(k, 0, -1):

        print(j, end="")

    print()