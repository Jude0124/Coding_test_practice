def solution(arr1, arr2):
    answer =[]
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    return answer


#     ```python
# import numpy as np

# def solution(arr1, arr2):
# 	return (np.array(arr1)+np.array(arr2)).tolist()
# ```