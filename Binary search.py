data = [12, 4, 67, 5, 34, 5, 8, 7]
value = 67


def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    data.sort()
    print(data)
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return data[middle]


print(binary_search(data, value))
