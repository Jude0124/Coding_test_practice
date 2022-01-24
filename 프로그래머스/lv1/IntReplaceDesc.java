import java.util.Arrays;
import java.util.Collections;

class IntReplaceDesc {
    public long intReplaceDesc(long n) {

        Integer[] sortBefore = new Integer[(int) Math.log10(n) + 1]; //log를 이용하여 자릿수를 구해준다
        int i = 0;                          
        String answer = "";

        for (String a : String.valueOf(n).split("")) {          //String으로 바꿔준뒤 split으로 array type으로  parsing해준다.
            sortBefore[i] = a.charAt(0) - '0';                  // char 형식으로 바꿔준뒤 ascii코드 값에 따라 '0'을 빼준다.
            i++;
        }
        Arrays.sort(sortBefore, Collections.reverseOrder());

        for (Integer a : sortBefore) {
            answer += a;
        }
        return Long.parseLong(answer);
    }
}
