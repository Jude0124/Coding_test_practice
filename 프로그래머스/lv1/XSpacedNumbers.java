class XSpacedNumbers {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long k = x;
        for( int i = 0; i < n ; i ++){
            answer[i] = k;
                k += x;
            
        }
        return answer;
    }
}