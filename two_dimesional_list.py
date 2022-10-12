def matrix(array):
    indexer = 0 
    for i in range(len(array)):
        if array[indexer][i] < 0: array[indexer][i] = 0
        else: array[indexer][i] = 1  
        indexer += 1
    return array


print(matrix([[-1, 4, -5, -9, 3], 
            [6, -4, -7, 4, -5], 
            [3, 5, 4, -9, -1], 
            [1, 5, -7, -8, -9], 
            [-3, 2, 1, -5, 6]]))


#User submitted solution
""" def matrix(arr):
    for z in range( len(arr) ):
        if arr[z][z] < 0:
            arr[z][z] = 0
        else:
            arr[z][z] = 1
    return arr """