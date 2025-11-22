---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 20:34:21
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
)

type Product struct {
	ID    int
	Name  string
	Price float64
}

func main() {
	m := make(map[int]Product)
	m[123] = Product{ID: 123, Name: "Product 1", Price: 321.123}
	m[456] = Product{ID: 456, Name: "Product 2", Price: 654.456}
	m[789] = Product{ID: 789, Name: "Product 3", Price: 987.789}

	for id, product := range m {
		fmt.Println(id, product)
	}
}
```

```shell
$ go run main.go
123 {123 Product 1 321.123}
456 {456 Product 2 654.456}
789 {789 Product 3 987.789}
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
>>       - [[🔖 map]]
