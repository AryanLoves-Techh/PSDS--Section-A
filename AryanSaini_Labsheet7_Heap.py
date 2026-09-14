class Heap:

    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] >= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = \
                self.heap[i], self.heap[parent]

            i = parent

    def pop(self):
        if not self.heap:
            return None

        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self.heapify(0, len(self.heap))

        return maximum

    def heapify(self, i, n):
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = \
                self.heap[largest], self.heap[i]

            i = largest

    def heap_sort(self, arr):

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify_array(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify_array(arr, i, 0)

        return arr

    def heapify_array(self, arr, n, i):

        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify_array(arr, n, largest)


h = Heap()

n = int(input("Enter number of priority queue elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    h.push(element)

print("\nPriority Queue:")

while h.heap:
    print(h.pop(), end=" ")

arr = list(map(int, input("\n\nEnter array elements separated by space: ").split()))

print("\nOriginal Array:", arr)

print("Sorted Array:", h.heap_sort(arr))
