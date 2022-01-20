class GetLCMWithGCD {
    public int[] getLCMWithGCD(int n, int m) {
        
        int[] answer = {getGCD(n,m),n*m/getGCD(n,m)};
        return answer;
    }
    
    public int getGCD(int a, int b){
        if (b == 0){ return a; } 
        return getGCD(b,a%b);
    }
}