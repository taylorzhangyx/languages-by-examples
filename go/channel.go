package main

import "fmt"

func main() {
	fmt.Print("start\n")

	dataStream := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Printf("data inserted: %v\n", i)
			dataStream <- i
		}
		close(dataStream)
	}()

	for v := range dataStream {
		fmt.Printf("value received: %v\n", v)
	}
}
