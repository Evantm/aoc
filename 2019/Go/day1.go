package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func gas(x int) int {
	return x / 3 - 2
}
func part_one() {
	sum_ := 0
	file, _ := os.Open("../python/day1.input")
	scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        i, _ := strconv.Atoi(scanner.Text())
        sum_ += gas(i) 

    }
    fmt.Println(sum_)
}

func part_two() {
	sum_ := 0
	file, _ := os.Open("../python/day1.input")
	scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        i, _ := strconv.Atoi(scanner.Text())
        temp := gas(i) 
        for temp > 0 {
        	sum_ += temp
        	temp = gas(temp)
        }
    }
    fmt.Println(sum_)
}

func main() {
	part_two()
}