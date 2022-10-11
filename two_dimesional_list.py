def matrix(array):
    indexer = 0 
    for i in range(len(array)):
        if array[indexer][i] < 0: array[indexer][i] = 0
        #print(array[indexer][i])
        indexer += 1    
    return array


print(matrix([[-1, 4, -5, -9, 3], 
            [6, -4, -7, 4, -5], 
            [3, 5, 4, -9, -1], 
            [1, 5, -7, -8, -9], 
            [-3, 2, 1, -5, 6]]))