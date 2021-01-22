import java.util.ArrayList;
import java.util.Scanner;

public class CP1 {
    static public void input()
    {
        int []ar={9, 8, 7, 6, 5, 4, 3, 2, 1};
        Scanner sc = new Scanner(System.in);
        int num= sc.nextInt();
        System.out.println(num);
        for (int i = 0; i <num ; i++) {
            System.out.print(1+" ");
        }
        System.out.println();
        ArrayList obj = new ArrayList();
//        for (int i:ar
//             ) {
//            while(num>=i){
//                int times = num/i;
//                while(times-->0){
//                    obj.add(i);
//                }
//                num = num%i;
//            }
//        }
//        System.out.println(obj.size());
//        obj.forEach(n-> System.out.print(n+" "));
//        System.out.println();
    }


    public static void main(String[] args) {
        input();
    }
}