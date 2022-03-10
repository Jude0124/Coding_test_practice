import java.util.*;
public class PhoneNumberList {
    public boolean solution(String[] phoneBook) {
        Arrays.sort(phoneBook);
        for (int i=0; i<phoneBook.length; i++){
            for (int j=i+1; j<phoneBook.length; j++){
                if (phoneBook[j].startsWith(phoneBook[i])){
                    return false;
                }
            }
        }
        return true;
    }
}
