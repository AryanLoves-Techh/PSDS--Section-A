def smallest_subarray(arr, target):
    left = 0
    total = 0
    ans = len(arr) + 1

    for right in range(len(arr)):
        total += arr[right]

        while total > target:
            ans = min(ans, right - left + 1)
            total -= arr[left]
            left += 1

    return -1 if ans == len(arr) + 1 else ans


arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target: "))

print("Smallest length:", smallest_subarray(arr, target))
