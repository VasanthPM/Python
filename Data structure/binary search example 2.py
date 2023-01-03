arr = []
n = int(input("Enter your array length : "))
for i in range(n):
    arr.append(int(input("Enter your Value : ")))
value = int(input("Enter Value to Search : "))
arr.sort()
print(arr)

def binay_search(arr,value):
    left = 0
    right = n-1

    while left <= right:
        middle = (left + right) // 2
        #print(left,right)
        if value < arr[middle]:
            right = middle - 1
        elif value > arr[middle]:
            left = middle + 1
        else:
            return (arr[middle])


print(binay_search(arr,value))


