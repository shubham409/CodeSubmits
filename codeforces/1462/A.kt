import java.util.*
import kotlin.math.max
import kotlin.math.min
fun main() {
    var io = Scanner(System.`in`)
    var t = io.nextInt()
    while (t-->0)
    {
        var n= io.nextInt()
        var array = Array<Int>(n){ io.nextInt() }
        solve(array,n)
    }
}
fun solve(array : Array<Int>, n:Int){
    var ans=Array<Int>(n){0}
//    two pointer technique
    var start=0
    var end=n-1
    var i=0
    while(start<=end){
        if (start<=end)
        {
            ans[i++]=array[start++]
        }
        if (start<=end)
        {
            ans[i++]=array[end--]
        }

    }
    for (i in ans){
        print("$i ")
    }
    println()

}