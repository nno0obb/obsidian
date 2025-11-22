---
created_at: 2025/05/12 00:18:19
updated_at: 2025/09/28 17:40:59
---
---

# # Overview

특정 파일의 UTI 조회합니다.

# # Details

## # What do?

```shell
$ touch asdf
$ mdls -name kMDItemContentType -name kMDItemContentTypeTree asdf
kMDItemContentType     = "public.data"
kMDItemContentTypeTree = (
    "public.data",
    "public.item"
)
```

```shell
$ touch fdsa.txt
$ mdls -name kMDItemContentType -name kMDItemContentTypeTree fdsa.txt
kMDItemContentType     = "public.plain-text"
kMDItemContentTypeTree = (
    "public.plain-text",
    "public.text",
    "public.data",
    "public.item",
    "public.content"
)
```

---

> [!info] Keywords
> - [[UTI]]

> [!tip] Refs
> - [[🌐 ChatGPT]]

> [!multi-column]
>
>> [!cite] Tags
>> - [[🏷️ command]]
>
>> [!example] Paths
>> - [[🔖 productivity_tool]]
>>   - [[🔖 cmd]]
>>     - [[🔖 mdls]]
