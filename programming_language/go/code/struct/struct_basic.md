---
created_at: 2025/06/14 22:48:34
updated_at: 2025/10/11 19:30:35
---
---
# # TSIA

```go
// main.go
package main

import "fmt"

type Person struct {
	Name   string
	Age    int
	Weight float64
}

func (p *Person) getAge() int {
	return p.Age
}

func main() {
	person := &Person{
		Name: "John",
		Age:  30,
	}
	fmt.Println(person)
	fmt.Println(person.Name)
	fmt.Println(person.getAge())
}
```

```shell
$ go run main.go
&{John 30 0}
John
30
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
>>      - [[🔖 struct]]
