---
created_at: 2025/05/12 00:18:19
updated_at: 2025/05/23 22:31:27
---
---

# # Overview

맥에서 `PATH` 환경변수를 추가하는 방법을 정리합니다.

# # Details

## # What do?

```shell
$ cat /etc/paths.d/home-bin
$HOME/bin
```

```shell
$ cat $HOME/bin/hi
echo hello
```

```shell
$ which hi
/Users/nno0obb/bin/hi
```

```shell
$ hi
hello
```

### # +a

```shell
$ echo "$PATH" | tr ':' '\n'
...
/usr/local/bin
/System/Cryptexes/App/usr/bin
/usr/bin
/bin
/usr/sbin
/sbin
...
```

```shell
$ cat /etc/paths
/usr/local/bin
/System/Cryptexes/App/usr/bin
/usr/bin
/bin
/usr/sbin
/sbin
```

---

> [!info] Keywords
> - N5B :: [[환경변수]]

> [!tip] Refs
> - [[🌐 ChatGPT]]

> [!example] Tags
> - [[🔖 mac]]
> - [[🔖 osx]]
> - [[🏷️ setup]]

> [!multi-column]
>
>> [!cite] Tags
>> - [[🏷️ setup]]
>
>> [!example] Paths
>> - [[🔖 mac]]
>>   - [[🔖 osx]]
