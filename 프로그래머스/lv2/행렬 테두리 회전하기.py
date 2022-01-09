def solution(rows, columns, queries):
    matrix = [[j+i*columns+1 for j in range(columns)] for i in range(rows)]
    answer = []
    for x1,y1,x2,y2 in queries:
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        temp = [matrix[x1][y1]] # 초기 유실 값 미리 save
        for i in range(x1+1,x2+1): 
            matrix[i-1][y1] = matrix[i][y1] # B -> T
            temp.append(matrix[i][y1])
        for i in range(y1+1,y2+1): 
            matrix[x2][i-1] = matrix[x2][i] #L -> R
            temp.append(matrix[x2][i])
        for i in range(x2,x1,-1):
            matrix[i][y2] = matrix[i-1][y2] # T -> B
            temp.append(matrix[i-1][y2])
        for i in range(y2,y1+1,-1): 
            matrix[x1][i] = matrix[x1][i-1] # R -> L
            temp.append(matrix[x1][i-1])
        matrix[x1][y1+1] = temp[0]
        answer.append(min(temp))
    return answer