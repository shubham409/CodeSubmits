import java.util.Scanner;public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test_cases = sc.nextInt();
        while (test_cases-->0)
        {
            String str1 = sc.next();
//            long value = Integer.parseInt(str1);
//            str1=String.valueOf(value);
            System.out.println(str1.length());
        }


    }
}