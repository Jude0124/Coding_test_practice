
import math
def solution(progresses, speeds):
  answer = []
  cnt = 1
  for i in range(len(progresses)):
    if i == 0 :
      cnt = 1
      pre = (math.ceil((100-progresses[i])/speeds[i]))
    elif (math.ceil((100-progresses[i])/speeds[i])) <=pre:
      cnt += 1
    else:
      answer.append(cnt)
      cnt = 1
      pre = (math.ceil((100-progresses[i])/speeds[i]))
  answer.append(cnt)
  return answer




