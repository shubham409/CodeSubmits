import java.util.*
import kotlin.math.max
import kotlin.math.min
fun main() {
    var io = Scanner(System.`in`)
    var t = io.nextInt()
    while (t-->0)
    {
        var temp1= io.nextInt()
        var temp2= io.nextInt()
        solve(temp1, temp2)
    }

}
fun solve(a:Int, b:Int){
    if(a==b) println(a+b)
    if(a>b) println(a+a-1)
    if(b>a) println(b+b-1)
}