import java.util.Scanner;


public class Run {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int size =sc.nextInt();
        int win = sc.nextInt();
        // ? input 
        int ar[] = new int[size];
        for (int i = 0; i < ar.length; i++) {
            ar[i] = sc.nextInt();
        }

        int score =ar[win-1];
        int sum=0;
        for (int i=0; i<ar.length;i++)
        {
            if (ar[i]>=score && ar[i]>0 ) sum++;
            
            
        }
      System.out.println(sum);
    }
}