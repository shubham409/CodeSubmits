import java.util.Scanner;


public class Run {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
       int ar[][] = new int[5][5];
       int x=0,y=0;
       for (int i = 0; i < ar.length; i++) {
           for (int j = 0; j < ar.length; j++) {
               ar[i][j]= sc.nextInt();
               if (ar[i][j]==1)
               {
                x=i+1;
                y=j+1;
               }
           }
       }
      System.out.println(Math.abs(3-x)+Math.abs(3-y)); 
    }
}