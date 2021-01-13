def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer+=i
        elif ((i.isupper() == True) and (ord(i)+n>90)) or ((i.isupper() == False) and (ord(i)+n>122)):
            answer+=chr(ord(i)+n-26)
        else:
            answer+=chr(ord(i)+n)
            
    
    return answer