package main
import(
	"fmt"
	"math"
)
func GreatPF(lim int)int {
	pf, gpf, c, i  := 0, 0, 0, 0
	if i = int(math.Sqrt(float64(lim))); (i % 2) == 0 {
		i--
	}
	for ; i > 1;  i = i - 2 {
		if ((lim % i) == 0) && (CheckPrime(i)){
			pf = i
			fmt.Println(c)
			return pf
		}
		c++
	}
	fmt.Println(c)
	return gpf
}
func CheckPrime(num int)bool{
	for i := 2; i <= int(math.Sqrt(float64(num))); i++{
		if (num % i) == 0 {
			return false
		}
	}
	return true

}


func main(){
	m := 600851475143	
	fmt.Println(GreatPF(m))
}
