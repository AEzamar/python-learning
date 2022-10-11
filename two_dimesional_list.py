def matrix(array):
    indexer = 0 
    for i in range(len(array)):
        print(array[indexer][i])
        indexer += 1
        """ for j in range(len(array)):
            print(array[j][i]) """
    return array


print(matrix([[-1, 4, -5, -9, 3], 
            [6, -4, -7, 4, -5], 
            [3, 5, 4, -9, -1], 
            [1, 5, -7, -8, -9], 
            [-3, 2, 1, -5, 6]]))