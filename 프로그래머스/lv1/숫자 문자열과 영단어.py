def solution(s):
    answer,temp,nums = "","",["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in s:
        if str.isdigit(i) == True:
            answer += i
        else:
            temp += i
            if temp in nums:
                answer += str(nums.index(temp))
                temp = ""
    return int(answer)