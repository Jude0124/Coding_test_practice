def solution(n):
    J = 1
    answer = 0
    n3 = []
    while n >= J:
        J *= 3  #n보다 큰 수가 될때까지 3의 거듭제곱 수행
    J /= 3        # 한번 나눠줌으로써 n보다 작은 수 중 가장 큰 거듭제곱 수 J 추출
    while J != 1/3:  # J가 1이될 때까지 수행
        n3.append(n//J) # 반복문 내에서 J로 나눠준후 몫을 저장
        n -= (n//J)*J # 나눈 값만 큼 n 값 초기화
        J /= 3        # J 값 초기화
    for j in range(len(n3)):
        answer+=(3**j)*n3[j]    # 리스트를 건드리지 않고 range를 이용하여 앞에서부터 차례로 10진화 후 합연산 
    return answer