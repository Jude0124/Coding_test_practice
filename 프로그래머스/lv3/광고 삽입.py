# dp + 투포인터

def solution(p,a,l):
    p,a = convert(p),convert(a)
    v = [0]*(p+1)
    
    for i in l:
        v[convert(i.split("-")[0])] += 1
        v[convert(i.split("-")[1])] -= 1     
    for i in range(1,len(v)):
        v[i] += v[i-1]
    for i in range(1,len(v)):
        v[i] += v[i-1]
        
    ans,answer = v[a],0 
    for i in range(1,p-a):
        if v[i+a]-v[i] > ans:
            ans = v[i+a] - v[i]
            answer = i+1
    return div(answer)

def convert(t):
    return int(t[0:2])*3600 + int(t[3:5])*60 + int(t[6:])

def div(t):
    time = ""
    time += str(divmod(t,3600)[0]).rjust(2,"0")
    t = divmod(t,3600)[1]
    time += ":"+str(divmod(t,60)[0]).rjust(2,"0") + ":" + str(divmod(t,60)[1]).rjust(2,"0")
    return time