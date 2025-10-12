---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 19:37:06
---
---
# # TSIA

```go
// main.go
package main

import "fmt"

func main() {
	arr := [...][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	for i, row := range arr {
		for j, num := range row {
			fmt.Printf("arr[%d][%d] = %d\n", i, j, num)
		}
	}
}
```

```shell
$ go run main.go
arr[0][0] = 1
arr[0][1] = 2
arr[0][2] = 3
arr[1][0] = 4
arr[1][1] = 5
arr[1][2] = 6
arr[2][0] = 7
arr[2][1] = 8
arr[2][2] = 9
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
>>      - [[🔖 array]]
