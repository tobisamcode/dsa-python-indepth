def binarysearch(arr, key, L, R):
    if L > R:
        return -1
    else:
        mid = (L + R) // 2

        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return  binarysearch(arr, key, L, mid - 1)
        elif key > arr[mid]:
            return binarysearch(arr, key, mid + 1, R)

array = [2, 3, 6, 8, 9, 11]
found = binarysearch(array, 10, 0, len(array))
print('Result:', found)