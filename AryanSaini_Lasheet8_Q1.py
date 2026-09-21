def maxSubarray(arr, k):
    WinSum = sum(arr[:k])
    maxSum = WinSum

    for right in range(k, len(arr)):
        WinSum += arr[right]
        WinSum -= arr[right - k]

        maxSum = max(maxSum, WinSum)

    return maxSum


n = int(input("Enter the size of array"))
k = int(input("Enter the size of contiguous array"))
arr = list(map(int, input().split()))

print(maxSubarray(arr, k))
