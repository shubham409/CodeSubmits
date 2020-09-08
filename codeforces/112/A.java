import java.util.Scanner;

public class Code11 {
    public static void main(String[] args) {
        String s,t;
        Scanner sc = new Scanner(System.in);
        s= sc.nextLine();
        t= sc.nextLine();
        
        s=s.toLowerCase();
        t=t.toLowerCase();

        int val = s.compareTo(t);
        if (val<0)
        val =-1;
        if (val>0)
        val = 1;
        System.out.println(val);
    }
}
