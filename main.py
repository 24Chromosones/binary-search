def binary_search(search_this, list_length, target):
    lower = 0
    higher = list_length - 1
    while lower <= higher:
        middle = (lower + higher) // 2
        if search_this[middle] < target:
            lower = middle + 1
        if search_this[middle] > target:
            higher = middle - 1
        else:
            return middle
    else:
        return "target not in list"

test = [2, 24, 34, 6, 456, 234, 12, 643, 123, 5, 3453, 12312, 3245]
test.sort()
print(test)
print(binary_search(test, len(test), 123))
