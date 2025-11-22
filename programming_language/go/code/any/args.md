---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 20:18:07
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
	"reflect"
)

func dotdotdot(args ...any) {
	for _, arg := range args {
		switch arg := arg.(type) {
		case bool:
			val := arg
			fmt.Println(reflect.TypeOf(val))
		case int:
			val := arg
			fmt.Println(reflect.TypeOf(val))
		case float64:
			val := arg
			fmt.Println(reflect.TypeOf(val))
		case string:
			val := arg
			fmt.Println(reflect.TypeOf(val))
		}
	}
}

func main() {
	dotdotdot(1, "2", 3.0, true)
}
```

```shell
$ go run main.go
int
string
float64
bool
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
>>       - [[🔖 any]]
