---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 18:46:45
---
---
# # TSIA

```go
// main.go
package main

import "fmt"

const (
	_ int = iota
	A
	B
	C
)

func main() {
	fmt.Println(A, B, C)
}
```

```shell
$ go run main.go
1 2 3
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
>>       - [[🔖 iota]]
