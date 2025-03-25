def insertionsort(A):
    n = len(A)
    for i in range(n):
        key = A[i]
        position = i

        while position > 0 and A[position-1] > key:
            A[position] = A[position-1]
            position = position - 1

        A[position] = key

A = [3,5,8,9,6,2]
print('original array: ',A)
insertionsort(A)
print('sorted array: ',A)