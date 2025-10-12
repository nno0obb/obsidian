---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 21:25:54
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
	"math/rand"
	"sync"
)

var count int = 0

func plus(no int, ch chan int) {
	val := <-ch
	count += val
	fmt.Printf("type: +, no: %d, val: %d, count: %d\n", no, val, count)
}

func minus(no int, ch chan int) {
	val := <-ch
	count -= val
	fmt.Printf("type: -, no: %d, val: %d, count: %d\n", no, val, count)
}

func main() {
	wg := sync.WaitGroup{}
	plusCh := make(chan int)
	minusCh := make(chan int)
	wg.Add(5)

	for i := range 5 {
		go func() {
			plus(i, plusCh)
			minus(i, minusCh)
			wg.Done()
		}()
		plusCh <- rand.Intn(10)
		minusCh <- rand.Intn(10)
	}
	wg.Wait()
}
```

```shell
$ go run main.go
type: +, no: 0, val: 5, count: 5
type: -, no: 0, val: 1, count: 4
type: +, no: 1, val: 1, count: 5
type: +, no: 2, val: 8, count: 13
type: +, no: 3, val: 5, count: 18
type: +, no: 4, val: 6, count: 24
type: -, no: 4, val: 9, count: 15
type: -, no: 1, val: 4, count: 11
type: -, no: 2, val: 4, count: 7
type: -, no: 3, val: 1, count: 6
```

---

> [!info] Keywords
> - ...

> [!tip] Refs
> - ...

> [!multi-column]
>
>> [!cite] Tags
>> - ...
>> - ...
>
>> [!example] Paths
>>  - [[🔖 programming_language]]
>>    - [[🔖 go]]
>>      - [[🔖 channel]]
