class GetAverage {
    public double getAverage(int[] arr) {
        double answer = 0;
    
        for(int value : arr) answer += value;
        
        return answer/arr.length;
    }
}