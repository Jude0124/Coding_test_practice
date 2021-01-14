class countpandy:
    def solution(self,s):
        s2 = s.lower()
        answer = True
        cnt = 0
        cnt2 = 0
        for i in s2:
            if i == "p":
                cnt += 1
            elif i == "y":
                cnt2 += 1
        if cnt != cnt2:
            answer = False
        return answer


    #  다른 사람의 풀이
    #  count 함수 하나면 for문 생략 가능

    def solution2(self,s):
        return s.lower().count("p") == s.lower().count("y")