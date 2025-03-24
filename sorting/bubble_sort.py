def bubblesort(array):
    n = len(array)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]


A = [3,5,8,9,6,2]
print('original array: ',A)
bubblesort(A)
print('sorted array: ',A)