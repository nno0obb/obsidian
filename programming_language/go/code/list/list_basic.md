---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 20:33:15
---
---
# # TSIA

```go
// main.go
package main

import (
	"container/list"
	"fmt"
)

func main() {
	lst := list.New()
	lst.PushBack(1)
	lst.PushBack(2)
	lst.PushFront(3)
	for e := lst.Front(); e != nil; e = e.Next() {
		fmt.Println(e.Value)
	}
	fmt.Println("====")
	for e := lst.Back(); e != nil; e = e.Prev() {
		fmt.Println(e.Value)
	}
}
```

```shell
$ go run main.go
3
1
2
====
2
1
3
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
>>      - [[🔖 list]]
