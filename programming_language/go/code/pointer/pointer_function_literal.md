---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 20:27:44
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
	"reflect"
	"runtime"
)

func getFunc(operator string) func(int, int) int {
	switch operator {
	case "+":
		return func(a, b int) int {
			return a + b
		}
	case "-":
		return func(a, b int) int {
			return a - b
		}
	case "*":
		return func(a, b int) int {
			return a * b
		}
	}
	return nil
}

func main() {
	operator := "+"
	_func := getFunc(operator)
	_func_ptr := reflect.ValueOf(_func).Pointer()
	_func_name := runtime.FuncForPC(_func_ptr).Name()
	fmt.Println(_func(1, 2), _func_name)
}
```

```shell
$ go run main.go
3 main.main.getFunc.func1
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
>>       - [[🔖 pointer]]
