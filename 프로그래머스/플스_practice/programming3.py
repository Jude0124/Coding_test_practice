def solution(n, edges, k, a, b):
    global board = [[0 for i in range(n)] for j in range(n)]
    global visited = [[0 for i in range(n)] for j in range(n)]
    for i in edges:
        board[i[0]][i[1]] = 1
        board[i[1]][i[0]] = 1
        visited[i[0]][i[1]] = 2
        visited[i[1]][i[0]] = 2
    print(board)
    answer = -1
    return answer

def dfs(start,k,depth):
    for  i in range(n):
        if (board[start][i] == 1):
            visited[start][i] == True
            visited[i][start] == True
            dfs(i,k,depth+1)
            visited[i][start] == False
            visited[start][i] == False
            
            