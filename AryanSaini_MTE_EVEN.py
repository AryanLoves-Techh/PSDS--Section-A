def findDistance(x, K):
    return bin(x ^ K).count('1')


def hammingSort():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        def key(x):
            return (findDistance(x, K), x)

        A.sort(key=key)
        print(*A)


hammingSort()
