import java.util.*
import kotlin.math.max
import kotlin.math.min
fun main() {
    var io = Scanner(System.`in`)
    var t = io.nextInt()
    while (t-->0)
    {
        var temp= io.nextInt()
        solve(temp)
    }

}
fun solve(temp:Int){
    var array= Array<Int>(temp){0}
    for (i in 1..array.size-1){
        array[i]=i
    }
    array[0]=array.size
    for (i in array){
        print( "$i ")
    }
    println()
}