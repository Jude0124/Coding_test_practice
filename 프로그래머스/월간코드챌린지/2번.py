def solution(s):
    cnt = 0
    for j in range(len(s)):
        tmp = s[j:]+s[0:j]
        cnt1, cnt2, cnt3 = 0,0,0
        for i in tmp:
            if i == "[":
                cnt1 += 1
            elif i == "]":
                cnt1 -= 1
            elif i == "(":
                cnt2 += 1
            elif i == ")":
                cnt2 -= 1
            elif i == "{":
                cnt3 += 1
            elif i == "}":
                cnt3 -= 1
            if (cnt1 < 0) or (cnt2 < 0) or (cnt3 < 0):
                cnt -= 1
                break
        else:
            if cnt1+cnt2+cnt3 != 0:
                cnt -= 1
    return len(s) + cnt