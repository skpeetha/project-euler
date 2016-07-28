package main
import(
	"fmt"
	"math"
)

func main(){
	n,i,j,c,t := 600851475143,2,2,0,0
	pf,gpf := 0,0
	for i <= int(math.Sqrt(float64(n))){
		for j <= int(math.Sqrt(float64(i))){
			if (i % j) == 0{
				c++
			}
			j++
		}
		if (c == 0)&&(n%i == 0){
			pf = i
			if pf > gpf{
				gpf = pf
			}
		}
		t = t + j
		j = 2
		c = 0
		i++
	}
	fmt.Println(gpf,t+j)
}
