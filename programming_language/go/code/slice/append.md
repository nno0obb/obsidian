---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 19:43:17
---
---
# # TSIA

```go
// main.go
package main

import "fmt"

func main() {
	slice1 := []int{1, 3: 2, 5: 3}
	slice2 := append([]int{}, slice1...)
	fmt.Println(slice2[1:5])
}
```

```shell
$ go run main.go
[0 0 2 0]
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
