---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 19:27:16
---
---
# # TSIA

```go
// main.go
package main

import "fmt"

func main() {
	str := "Hello, 월드!"
	for i, v := range []rune(str) {
		fmt.Printf("%d %c\n", i, v)
	}
	fmt.Println("====")
	for i, v := range str {
		fmt.Printf("%d %c\n", i, v)
	}
}
```

```shell
$ go run main.go
0 H
1 e
2 l
3 l
4 o
5 ,
6  
7 월
8 드
9 !
====
0 H
1 e
2 l
3 l
4 o
5 ,
6  
7 월
10 드
13 !
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
>>       - [[🔖 string]]
