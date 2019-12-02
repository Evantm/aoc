package main

import (
	"fmt"
	"bufio"
)

func main() {
	file, err := os.Open("day1.input")
	scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        fmt.Println(scanner.Text())
    }
}