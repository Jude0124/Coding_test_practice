
class CollatzConjecture {
    public int collatzConjecture(long num) {
        int cnt = 0; 
        while(cnt !=500){
            
            if (num == 1){   
            return cnt;  
            }          
            
            cnt++;      
            
            if(num%2==0){        
                num /= 2;  
                
            }else{        
                num = num*3 + 1;
            }
        }
        return -1;
    }
}