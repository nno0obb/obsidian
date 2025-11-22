---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 20:19:51
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
	defer fmt.Println("3")
	defer fmt.Println("2")
	defer fmt.Println("1")
}
```

```shell
$ go run main.go
1
2
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
>> - [[🔖 programming_language]]
>>   - [[🔖 go]]
>>     - [[🔖 code]]
>>       - [[🔖 defer]]
