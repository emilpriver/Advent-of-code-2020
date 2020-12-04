package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	file, err := ioutil.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	splits := strings.Split(string(file), "\n\n")
	fmt.Println(splits[4])
}
