public class NaturalReverse {
        public int[] naturalReverse(long n) {
            int[] answer = new int[(int)Math.log10(n)+1];
            for (int i = 0 ; i < answer.length ; i++){
                answer[i] = (int)(n%10);
                n /= 10;
            }
            return answer;
        }
    }

