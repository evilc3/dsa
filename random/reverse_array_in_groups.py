n = 5
k = 3
arr = [1,2,3,4,5,6,7,8]
# arr = [5,6,8,9]

for i in range(0,len(arr),k):
    n = min(i + k, len(arr))
    # n = k if i + k < len(arr) else len(arr) - i
    print(i, i + k, n)
    j = i
    while (n - j) // 2 > 0 and j < len(arr):
    # while n // 2 > 0:
        print(n-1,j)
        arr[n-1], arr[j] = arr[j], arr[n-1]
        n -= 1
        j += 1
    
    print(arr)

print(arr)

[17,5,2]