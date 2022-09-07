class testingPersonalityCases {
    static int R , T ,  C , F , J , M , A ,N;
    static int[] sheet = {R, T, C, F, J, M, A, N};
    static char[] chars =  {'R','T','C',"F",'J','M','A','N'};
    
    public String testingPersonalityCases(String[] survey, int[] choices) {
    
        R = T =  C = F = J = M = A = N = 0;
    
        for ( int i = 0; i < survey.length; i++){
                checkIndex(survey[i],4-choices[i]);
        }
    
    
        return getAnswer();

        }
    
    void checkIndex(String eliment , int score){
        char abc;
        if (score == 0){
            return; 
        }else if (score < 0 ){
            abc = eliment.charAt(0);   
        }else {
            abc =  eliment.charAt(1);
        }

        for (int i = 0 ; i < chars.length ; i++){
            if (chars[i] == abc){
                sheet[i] += Math.abs(score); 
                }
        }
       
        return;
    }

    String getAnswer(){
        String answer = "";
        for (int i = 0 ; i <7;i += 2){
            if(sheet[i] <= sheet[i+1]){
                answer += chars[i];
            }
            else{
                answer += chars[i+1];
            }
        }
        return answer;
    }
    }

// 지표는 총 8가지가 존재
// 8가지는 한쌍씩 총 4쌍으로 비교 되며
// 한쌍내에서 점수가 상쇄되어 계산되지는 않음


//  풀이 로직

//  1. 우선 각각의 성격에 대하여 빈 변수를 할당해준다.
//  2. 각 변수에 대하여 