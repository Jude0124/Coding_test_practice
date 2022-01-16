def solution(price, money, count):
    if ((count*(count+1))/2)*price > money : return ((count*(count+1))/2)*price - money
    return 0