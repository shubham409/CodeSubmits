    import java.util.Scanner;
     
    public class A_Word_Capitalization {
     
        public static void main(String[] args) {
            Scanner sc =new Scanner(System.in);
            String s=sc.next();
            
            System.out.println(s.substring(0,1).toUpperCase()+s.substring(1));
        }
    }