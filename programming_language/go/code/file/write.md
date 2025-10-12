---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 21:26:01
---
---
# # TSIA

```go
// main.go
package main

import (
	"fmt"
	"os"
)

const filename = "temp.txt"

func main() {
	text := `a
bc
def
ghij
klmno
pqrstu
`
	err := os.WriteFile(filename, []byte(text), 0644)
	if err != nil {
		fmt.Println(err)
		return
	}
	file, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("%s", file)
}
```

```shell
$ go run main.go
a
bc
def
ghij
klmno
pqrstu
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
>>      - [[🔖 file]]
