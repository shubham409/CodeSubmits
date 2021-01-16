import java.util.ArrayList;
import java.util.Scanner;
import java.math.*;
public class Code2 {
    static public void input()
    {
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
        while (T-->0){
            int capacity = sc.nextInt();
            ArrayList< Integer> one = new ArrayList<>(capacity);
            for (int i = 0; i <capacity ; i++) {
                one.add(sc.nextInt());
            }
            capacity = sc.nextInt();
            ArrayList< Integer> two = new ArrayList<>(capacity);
            for (int i = 0; i <capacity ; i++) {
                two.add(sc.nextInt());
            }
            output(one,two);
        }
    }
    static public void output(ArrayList <Integer> one,ArrayList <Integer> two)
    {
        int sum1=0;
        int sum2=0;
        int prefixsum1[] = new int [one.size()];
        int prefixsum2[] = new int [two.size()];
        for (int i = 0; i < one.size(); i++) {
            if (i==0){
                prefixsum1[i]=one.get(i);

            }
            else {
                prefixsum1[i] =one.get(i)+prefixsum1[i-1];
            }
            sum1= Math.max(prefixsum1[i],sum1);
        }
        for (int i = 0; i < two.size(); i++) {
            if (i==0){
                prefixsum2[i]=two.get(i);
            }
            else prefixsum2[i] =two.get(i)+prefixsum2[i-1];

            sum2= Math.max(prefixsum2[i],sum2);
        }
        System.out.println(sum1+sum2);

    }
    public static void main(String[] args) {
        input();

    }
}
