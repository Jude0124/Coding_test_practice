class HarshadNumber {
    public boolean harshadNumber(int x) {
        boolean answer = false;
        int Num = x;
        int SplitNumberSum = 0; 
        
        while (Num!=0){
            
        SplitNumberSum += Num%10;
        Num = Num/10;
            
        }
        if (x%SplitNumberSum == 0){
            answer = true;
        }
        
        return answer;
    }
}