import java.util.Scanner;

public class Run {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int i = sc.nextInt();
        int j = sc.nextInt();
        System.out.println((int)Math.floor(i*j/2) );
    }
    
}