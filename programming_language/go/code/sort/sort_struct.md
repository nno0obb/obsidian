---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 20:11:14
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
	"sort"
)

type Student struct {
	Name string
	Age  int
}

type Students []Student

func (s Students) Len() int {
	return len(s)
}

func (s Students) Less(i, j int) bool {
	return s[i].Age < s[j].Age
}

func (s Students) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func main() {
	s := Students{
		{Name: "A", Age: 50},
		{Name: "B", Age: 30},
		{Name: "C", Age: 40},
		{Name: "D", Age: 10},
		{Name: "E", Age: 20},
	}
	sort.Sort(s)
	fmt.Println(s)
}
```

```shell
$ go run main.go
[{D 10} {E 20} {B 30} {C 40} {A 50}]
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
>>      - [[🔖 sort]]
