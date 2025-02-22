def linearsearch (arr, key):
    index = 0
    while index < len(arr):
        if arr[index] == key:
            return index
        index += 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 5


print(linearsearch(arr, key))