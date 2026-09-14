def maximize_difference(arr):
    n = len(arr)

    if n <= 1:
        return arr, 0

    arr.sort()
    result = []

    if n % 2 == 0:
        mid = n // 2

        for i in range(mid - 1):
            result.append(arr[i + 1])
            result.append(arr[n - 1 - i])

        result.append(arr[0])
        result.append(arr[mid])

    else:
        mid = n // 2

        result.append(arr[mid])

        for i in range(1, mid + 1):
            if mid + i < n:
                result.append(arr[mid + i])
            result.append(arr[mid - i])

    total = 0

    for i in range(1, n):
        total += abs(result[i] - result[i - 1])

    return result, total

arr = list(map(int, input("Enter array elements: ").split()))

result, total = maximize_difference(arr)

print("Rearranged array:", result)
print("Total sum:", total)
