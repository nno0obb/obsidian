---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 19:03:03
---
---
# # TSIA

```go
// main.go
package main

import "fmt"

func main() {
	switch a := 2; a {
	case 1, 2:
		fmt.Println("1, 2")
		fallthrough
	case 3:
		fmt.Println("3")
	case 2 + 2:
		fmt.Println("2 + 2")
	default:
		fmt.Println("default")
	}
}
```

```shell
$ go run main.go
1, 2
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
>>      - [[🔖 switch]]

