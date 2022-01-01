def inspect(case):
    for x,y,a in case:
        if a == 0:
            if y != 0 and (x,y-1,0) not in case and (x-1,y,1) not in case and \
            (x,y,1) not in case:
                return True
        else:
            if not ((x-1,y,1) in case and (x+1,y,1) in case) and \
            (x,y-1,0) not in case and (x+1,y-1,0) not in case:
                return True
    return False

def solution(n,build):
    case = set()
    for x,y,a,b in build:
        now = (x,y,a)
        if b:
            case.add(now)
            if inspect(case):
                case.remove(now)
        else:
            case.remove(now)
            if inspect(case):
                case.add(now)
                
    return sorted(map(list,case))

# 기둥과 보의 설치 및 제거 조건에 대한 함수를 만든 후 set에 값을 추가할때마다 설치/제거가 가능한지 확인 후,
# 해당 작업이 불가능 하다면 백업해준다.
# 모든 작업을 진행후 출력.