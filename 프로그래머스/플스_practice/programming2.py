#  제한사항
#  1 ≤ grid의 길이(=행의 개수) ≤ 9
#  1 ≤ grid의 각 행의 길이(=열의 개수) ≤ 9
#  1 ≤ grid 내 '?'의 개수 ≤ 9

#  입출력 예
#  grid	result
#  ["??b", "abc", "cc?"]	2
#  ["abcabcab","????????"]	0
#  ["aa?"]	3

# 격자가 존재할때 1차원 문자열 배열 grid가 매개변수로 주어지고 
#  주변 ? 를 모두 a,b,c 로 바꿀 수 있을때 같은문자인데 상하좌우로 
# 연결이 안되는 문자가 있어서는 안됨