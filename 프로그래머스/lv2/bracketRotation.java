// 문제 구상 알고리즘 순서
// 1. 나머지 정리를 이용하여 순환하는 이중 for (0,1,2,3,4,5 -> 1,2,3,4,5,0 -> ...) 구조 생성 why? 문자열의 인덱싱을 위해
// 2. 하나의 case에 대하여 isValid 메서드를 호출하여 온전한 문자열이면 answer++ , 그렇지 않으면 -- 해준다.
// 3. isValid(원본 문자열, 탐색 시작 index(괄호회전을 위해서)) 내부에서 Stack을 이용한다(후입선출 LIFO)
// 3-1. 여는 괄호일 경우 무지성으로 stack에 넣어준다.(add)
// 3-2. 닫는 괄호일 경우 아래와 같은 사항을 체크해준다.
// 3-2-1. 닫는 괄호가 들어가려 하는데(이하 peek) 이미 빈 문자열이면 올바른 문자열이 아니므로 retunr false
// 3-2-2. peek 했는데 해당 닫는 괄호와 짝이 맞지 않다면 올바른 문자열이 아니므로 return false
// 3-2-3. peek 했는데 해당 닫는 괄호와 짝이 맞다면 해당 여는 괄호를 pop 해준다(떠안고 사라짐)
// 4-1. 완전한 문자열이라면 add와 pop의 횟수가 정확히 맞아떨어져야 하므로 빈문자열이 아닐경우 return false
// 4-2. 위 모든 케이스를 통과할 경우 return true

import java.util.Stack;
public class bracketRotation {
    public static void main(String[] args) {    //테케
        solution("[](){}");
        solution("}]()[{");
        solution("[)(]");
        solution("}}}");
    }

    public static int solution(String s) {  
        int answer = 0;
        
        for (int i = 0; i < s.length(); i++) { //문자열을 length만큼 회전하며 탐색
            if(isValid(s,i)){
                answer++;
            }
        }
        return answer;
    }

    public static boolean isValid(String s, int i){
        Stack<String> stack = new Stack<>();
        for(int j = 0; j < s.length();j++){                    
            String temp = String.valueOf(s.charAt((i+j)%s.length()));          // 나머지 정리를 이용하여 한번의 case에 대하여 index 시작위치 설정
            if (temp.equals("[")  ||temp.equals("{")  || temp.equals("(") ){   // 시작 기호면 무지성으로 넣어준다.
                stack.add(temp);                            
            }else{
                if(stack.empty()){                                             // 종료기호인데 이미 stack이 비어있으면 종료기호로 시작하는 것이므로 false
                    return false;
                }
                else if(temp.equals("]") ){                                    // 이하 각각의 종료 기호에 대하여 짝이 안맞으면 false 맞다면 삭제

                    if(stack.peek().equals("[")){
                        stack.pop();
                    }else{
                        return false;
                    }
                }
                else if(temp.equals("}")){
                    if(stack.peek().equals("{")){
                        stack.pop();
                    }else{
                        return false;
                    }
                }else{
                    if(stack.peek().equals("(")){
                        stack.pop();
                    }else{
                        return false;
                    }
                }
            }
        }
        if(!stack.empty()){                                                 // 완전한 문자열이 아닐 경우(시작했지만 닫히지 않은 경우) false
            return false;
        }
        return true;                                                        // 완전한 문자열
    }
}
