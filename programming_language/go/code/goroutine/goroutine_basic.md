---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 21:04:28
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	wg := sync.WaitGroup{}
	
	wg.Add(2)
	go func() {
		str := "가나다라"
		for _, v := range str {
			fmt.Printf("%c", v)
			time.Sleep(1 * time.Second)
		}
		wg.Done()
	}()
	go func() {
		str := "1234"
		for _, v := range str {
			fmt.Printf("%c", v)
			time.Sleep(1 * time.Second)
		}
		wg.Done()
	}()
	
	wg.Wait()
}
```

```shell
$ go run main.go
가12나다3라4
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
>>      - [[🔖 goroutine]]
