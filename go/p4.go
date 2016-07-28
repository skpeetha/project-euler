package main
import(
	"fmt"
)

func CheckPalindrome(num int)bool{
	rev, rem  := 0, 0
	n := num
	for n != 0{
		rem = n % 10
		rev = rev * 10 + rem
		n /= 10
	}
	if num == rev {
		return true
	}
	return false
}

func main(){
	i, j, c := 999, 998, 0
	rec, gre := 0, 0
	for i > 100 {
		if CheckPalindrome(i * j){
			rec = i * j
			if rec > gre{
				gre = rec
			}	
		}
		j--
		if j < 100 {
			i--
			j = i - 1
		}
		c++
	}
//	fmt.Printf("%v * %v = %v\n", i, j, i * j)
	fmt.Println(c,gre)
}
