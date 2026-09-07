def fabonacci(n):
    a, b = 0, 1

    print("Fabonacci Series:")
    for i in range(n + 1):
        print(a , end = " ")
        a, b = b, a + b

n = int(input("Enter the number of elements"))
fabonacci(n)
