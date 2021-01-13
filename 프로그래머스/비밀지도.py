def converter(n,num):
    temp = []
    double = ""
    for i in range(n,0,-1):
        temp.append(num//2**(i-1))
        num -= (2**(i-1))*(num//2**(i-1))

    for v in temp:
        if v == 0:
            double += " "
        else:
            double += "#"     

    return double

def adder(x,y):
    answer = []
    for i in range(len(x)):
        temp = ""
        for j in range(len(x[i])):
            if x[i][j] == y[i][j]:
                temp+=(x[i][j])
            else:
                temp += "#"
        answer.append(temp)
    return answer

def solution(n, arr1, arr2):
    conv1 = []
    conv2 = []
    for i in range(len(arr1)):
        conv1.append(converter(n,arr1[i]))
        conv2.append(converter(n,arr2[i]))

    return adder(conv1,conv2)