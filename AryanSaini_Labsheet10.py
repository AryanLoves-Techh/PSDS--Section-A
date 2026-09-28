def digit_sum(x):
    return sum(map(int, str(abs(x))))


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    freq = {}
    answer = 0

    for x in nums:
        s = digit_sum(x)

        answer += freq.get(s, 0)

        freq[s] = freq.get(s, 0) + 1

    print(answer)


solve()
