def solution(board, moves):
    lis = []
    answer = 0
    for k in moves:
        for i in range(len(board)):
            if board[i][k-1] != 0 :
                lis.append(board[i][k-1])
                board[i][k-1] = 0
                break 
        try: 
            if lis[-1] == lis[-2]:
                lis.pop()
                lis.pop()
                answer+=2
        except IndexError:
            pass
    return answer