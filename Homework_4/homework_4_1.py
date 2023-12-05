
def trans_matrix(arr):
    trans_m = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    return trans_m


m = [[4, 7, 2], [3, 8, 1]]
print(m)
print(trans_matrix(m))
