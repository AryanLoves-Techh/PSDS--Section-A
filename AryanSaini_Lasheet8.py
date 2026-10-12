#Question 1
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

#Question2
def longest_substring(s):
    freq = [0] * 26

    left = 0
    ans = 0

    for right in range(len(s)):
        index = ord(s[right]) - ord('a')
        freq[index] += 1

        while freq[index] > 1:
            left_index = ord(s[left]) - ord('a')
            freq[left_index] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


s = input("Enter the String").strip()
print(longest_substring(s))

#Question 3
import heapq

def shortest_path(n, m, k, edges):
    graph = [[] for _ in range(n + 1)]

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    INF = float('inf')
    dist = [[INF] * (k + 1) for _ in range(n + 1)]

    pq = [(0, 1, 0)]
    dist[1][0] = 0

    while pq:
        cost, node, used = heapq.heappop(pq)

        if cost != dist[node][used]:
            continue

        if node == n:
            return cost

        if used == k:
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            new_used = used + 1

            if new_cost < dist[neighbor][new_used]:
                dist[neighbor][new_used] = new_cost
                heapq.heappush(
                    pq,
                    (new_cost, neighbor, new_used)
                )

    return -1



n, m, k = map(int, input("Enter paths").split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

print(shortest_path(n, m, k, edges))
