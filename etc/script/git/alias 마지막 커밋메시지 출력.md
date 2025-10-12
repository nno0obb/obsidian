---
created_at: 2025/09/06 18:01:23
updated_at: 2025/09/06 18:48:12
---
```
$ cat ~/.gitconfig
...
[alias]
    last = "!/usr/bin/env bash -c 'printf %s \"\$(git --no-pager log -1 --pretty=%B)\"'"
...
```
