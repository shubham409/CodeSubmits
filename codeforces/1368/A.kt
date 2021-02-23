import java.util.*
import kotlin.math.max
import kotlin.math.min
fun main() {
    solve()
}
fun solve(){
    var io = Scanner(System.`in`)
    var n: Int= io.nextInt()
    while (n-->0){
        var x=io.nextInt()
        var y=io.nextInt()
        var n=io.nextInt()
        var count:Int=0
        var a= max(x,y )
        var b= min(x,y)

        while (a<=n && b<=n){
            val tempa :Int= a
            val tempb: Int = b
            b=tempa
            a=tempa+tempb
            count++
        }
        println(count)

    }
}