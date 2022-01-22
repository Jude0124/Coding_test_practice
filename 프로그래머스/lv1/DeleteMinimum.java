class DeleteMinimum {
    public int[] deleteMinimum(int[] arr) {
        
        int minimum = arr[0];             // 문제 풀이후 ArrayList의 remove를 이용하여 for을 한번만 사용하는 좀 더 간단한 로직으로 접근하려했으나,
        int [] answer;                    // ArrayList<Integer>를 int[] array로 casting 하는 과정이 오히려 더 복잡해질 수 있어 현재 방법 고수
        for (int value : arr){            // to do list : 해당 casting을 진행하는데 있어 가장 간결한 하나의 용법을 정리하가.
            if (value < minimum){         // 또한 성능에 있어서도 remove 또한 결국 for와 같은 시간복잡도를 지녔기때문에 코드의 가독성에만 차이가 있을 것으로 판단함.
                minimum = value;
            }
        }
        
        if (arr.length == 1){
            answer = new int[1];
            answer[0] = -1;
        }else{
            answer = new int[arr.length-1];    
        }
        
        
        int idx = 0 ;
        for (int value : arr){
            if (value != minimum){
                answer[idx] = value;
                idx++;    
            }
        }
        
        return answer;
    }
}