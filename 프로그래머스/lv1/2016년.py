def solution(a,b):
    whatday = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31,29,31,30,31,30,31,31,30,31,30]
    if a==1:
        answer = whatday[b%7-1]
    else:
        answer = whatday[(sum(month[:a-1])+b)%7-1]
    return answer