package main

import (
	"fmt"
	"math"
)
func Fib(lim int) int{
	sum, f, n ,t :=0, 1, 2, 0
	for f <= lim{
		if f%2 == 0 {
			sum = sum + f
		}
		t = n
		n = n + f
		f = t
//fmt.Println(f,sum)	
	}
fmt.Println(f,n,t)	
        return sum

}

func main(){
	fmt.Println(Fib(int(4*math.Pow(10,6))))
	fmt.Println(Fib(10))
}


