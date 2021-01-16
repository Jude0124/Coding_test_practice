def solution(s):
    ans = []
    if len(s) == 1:
        ans = [1]
    else:
        for i in range(1,len(s)//2+1):
            cnt = 0
            tmp = [s[j:j+i] for j in range(0,len(s),i)]
            sen = ""
            for k in range(0,len(tmp)-1): 
                if tmp[k] == tmp[k+1]:
                    cnt += 1
                else:
                    if cnt != 0:
                        sen += str(cnt+1)
                        sen += tmp[k]
                        cnt = 0
                    else:
                        sen += tmp[k]
                        cnt = 0
            if cnt == 0:
                sen += tmp[k+1]
            else:
                sen += str(cnt+1)
                sen += tmp[k]
            ans.append(len(sen))

    return min(ans)