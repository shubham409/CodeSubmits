import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Code15
 */
public class Code15 {
    public static Boolean isVovel(char ar) {
        return ar=='a' || ar=='e' || ar=='i' || ar=='o' || ar=='u' || ar == 'y' ;
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        char [] ar= sc.next().toLowerCase().toCharArray();

        for (char c : ar) {
            
            
            if(!Code15.isVovel(c))
            System.out.print('.'+ String.valueOf(c));
        }
        
    }
}