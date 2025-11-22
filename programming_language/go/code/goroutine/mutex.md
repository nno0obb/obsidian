---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 21:14:11
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
	"sync"
)

var mutex sync.Mutex
var count int = 0

func plus(no int) {
	mutex.Lock()
	count++
	fmt.Printf("no: %d, count: %d\n", no, count)
	mutex.Unlock()
}

func minus(no int) {
	mutex.Lock()
	count--
	fmt.Printf("no: %d, count: %d\n", no, count)
	mutex.Unlock()
}

func main() {
	wg := sync.WaitGroup{}
	wg.Add(5)

	for i := 0; i < 5; i++ {
		go func() {
			plus(i)
			minus(i)
			wg.Done()
		}()
	}
	wg.Wait()
}
```

```shell
$ go run main.go
no: 4, count: 1
no: 4, count: 0
no: 1, count: 1
no: 1, count: 0
no: 0, count: 1
no: 0, count: 0
no: 2, count: 1
no: 2, count: 0
no: 3, count: 1
no: 3, count: 0
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
>> - [[🔖 programming_language]]
>>   - [[🔖 go]]
>>     - [[🔖 code]]
>>       - [[🔖 goroutine]]
