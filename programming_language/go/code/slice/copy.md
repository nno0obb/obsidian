---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 19:47:30
---
---
# # TSIA

```go
// main.go
package main

import "fmt"

func main() {
	slice1 := []int{1, 2, 3, 4, 5}
	slice2 := make([]int, 3, 10)
	_ = copy(slice2, slice1)
	fmt.Println(slice2)
}
```

```shell
$ go run main.go
[1 2 3]
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
>>      - [[🔖 slice]]
