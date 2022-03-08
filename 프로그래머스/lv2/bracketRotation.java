// 문제 구상 알고리즘 순서
// 0. 1~4번까지를 String의 length만큼 계속 반복한다.
// 1. 하나의 String에 대하여 for안에서 세 변수-> cnt1(대괄호) cnt2(중괄호) cnt3(소괄호)를 세준다.
// 2. 열림 기호는 ++ 닫힘기호는 -- 가 연산되게끔해준다.
// 3-1. 단 한번이라도 세변수들중 하나가 음수가 된다면(-기호가 먼저 등장한다면) 해당 String은 올바른 괄호문자열이 아니므로 해당 탐색을 break한다.
// 3-2. 끝까지 세변수가 음수가 된적이 없다면 변수 int answer 에 ++한다.
// 4. 맨앞의 한 기호를 빼서 맨뒤로  넣어준다 (stack이나 que 사용 가능할 듯)


class Solution {
    public int solution(String s) {
        int answer = -1;
        return answer;
    }
}