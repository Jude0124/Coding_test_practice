public class WeirdString {
    public String weirdString(String s) {
        s = s.toUpperCase();

        int cnt = 1;
        for (int i = 0; i < s.length(); i++) {
            if (' ' == s.charAt(i)) {
                cnt = 1;
            } else {
                if ((cnt % 2) == 0) {
                    String low = s.toLowerCase();
                    s = s.substring(0, i) + low.substring(i, i + 1) + s.substring(i + 1);
                }
                cnt++;
            }
        }
        return s;
    }
}
