def solution(dist):
    Merged = [value for array in dist for value in array]

    Max_Val = max(Merged)
    
    for i in range(0,len(Merged)):
        if(Merged[i] == Max_Val):
            index = i//len(dist)
            break;
    dic = {dis : i  for i,dis in enumerate(dist[index])}

    answer = []

    ans1 = [value for key,value in sorted(dic.items())]
    ans2 = [value for key,value in sorted(dic.items(),reverse=True)]
    
    answer.append(ans1)
    answer.append(ans2)
    return answer