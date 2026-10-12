def solve():
    n = int(input("Enter N: "))

    A = list(map(int, input("Enter array: ").split()))

    if all(x == A[0] for x in A):
        print(abs(A[0]))
    else:
        print(-1)


T = int(input("Enter number of test cases: "))

for _ in range(T):
    solve()
