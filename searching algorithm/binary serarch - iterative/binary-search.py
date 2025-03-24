def binarysearch(arr, key):
    L = 0
    R = len(arr) - 1
    while L <= R :
        mid = (L + R) // 2
        if (arr[mid] == key):
            return mid
        elif (arr[mid] > key):
            R = mid - 1
        elif (arr[mid] < key):
            L = mid + 1
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
found = binarysearch(array, 10)
print('Result:', found)
