---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 20:56:36
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
)

func main() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("recover", r)
		}
	}()
	panic("panic")
}
```

```shell
$ go run main.go
recover panic
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
>>      - [[🔖 panic]]
