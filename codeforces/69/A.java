import java.util.Scanner;

public class CP1 {
    static public void input()
    {
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
        Vector obj =new Vector();
        while (T-->0){
            obj=obj.add(new Vector(sc.nextInt(),sc.nextInt(),sc.nextInt()));
        }
        if (obj.isZero()) System.out.println("YES");
        else System.out.println("NO");
    }


    public static void main(String[] args) {
        input();
    }
}
class Vector
{
    int a,b,c;
    Vector(){
        a=0;
        b=0;
        c=0;
    }
    Vector(int a,int b,int c){
        this.a=a;
        this.b=b;
        this.c=c;
    }
    public Vector add(Vector obj){
        this.a=this.a+obj.a;
        this.b=this.b+obj.b;
        this.c=this.c+obj.c;
        return this;
    }
    public boolean isZero()
    {
        return a == 0 && b == 0 && c == 0;
    }
}
