---
created_at: 2025/08/31 17:23:33
updated_at: 2025/08/31 17:23:38
---
---

```python
"""
# 리트코드
# No. 393 / utf-8-validation
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        while idx < len(data):
            msb = data[idx].bit_length()
            if msb == 8:
                if (data[idx] >> 5) == 0b110:
                    cnt = 1
                elif (data[idx] >> 4) == 0b1110:
                    cnt = 2
                elif (data[idx] >> 3) == 0b11110:
                    cnt = 3
                else:
                    return False

                for _ in range(cnt):
                    idx += 1
                    if idx >= len(data):
                        return False
                    if (data[idx] >> 6) != 0b10:
                        return False
            idx += 1
        return True


def test_solution(subtests):
    with subtests.test("Example 1"):
        data = [197, 130, 1]
        output = True
        assert Solution().validUtf8(data) == output
    with subtests.test("Example 2"):
        data = [235, 140, 4]
        output = False
        assert Solution().validUtf8(data) == output
    with subtests.test("Example 3"):
        data = [237]
        output = False
        assert Solution().validUtf8(data) == output

```

---

> [!info] Keywords
> - ...

> [!tip] Refs
> - LeetCode :: [393. utf-8-validation](https://leetcode.com/problems/utf-8-validation)
> - GitHub :: [algorithm-ps/leetcode/393-utf-8-validation](https://github.com/nno0obb/algorithm-ps/tree/main/leetcode/393-utf-8-validation)

> [!multi-column]
>
>> [!cite] Tags
>> - [[🏷️ python3]]
>> - [[🏷️ solution]]
>
>> [!example] Paths
>> - [[🔖 computer_science]]
>>   - [[🔖 algorithm]]
>>     - [[🔖 ps]]
>>       - [[🔖 leetcode]]
