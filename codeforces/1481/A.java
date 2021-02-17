import java.util.HashMap;
import java.util.Scanner;

public class Code4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            boolean canx=false;
            boolean cany=false;
            StringBuilder sb = new StringBuilder(sc.next());
            HashMap<Character, Integer> hm = new HashMap<>();
            hm.put('U',0);
            hm.put('D',0);
            hm.put('L',0);
            hm.put('R',0);
            for (int i = 0; i < sb.length(); i++) {
                int count;
                    count= hm.get(sb.charAt(i));
                hm.put(sb.charAt(i), count + 1);
            }
            if(x>=0){
                if (hm.get('R') != null )
                {
                    if (hm.get('R')>=x) {
//                        System.out.println(hm.get('R'));
                        canx = true;
                    }
                }
            }
            else {
                if (hm.get('L') != null )
                {
                    if (hm.get('L')>= Math.abs(x)) canx=true;
                }
            }
            if(y>=0){
                if (hm.get('U') !=null )
                {
//                    System.out.println(hm.get('U') +y);
                    if (hm.get('U')>=y) {
//                        System.out.println(hm.get('U'));
                        cany = true;
                    }
                }
            }
            else {
                if (hm.get('D') !=null)
                {
                    if (hm.get('D')>= Math.abs(y)) cany=true;
                }
            }
//            System.out.println(hm);
            if(canx && cany) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}
