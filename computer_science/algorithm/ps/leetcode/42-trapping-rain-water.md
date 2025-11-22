---
created_at: 2025/07/24 23:15:13
updated_at: 2025/07/24 23:15:29
---
---

```python
"""
# 리트코드
# No. 42 / trapping-rain-water
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = -1
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i - 1])

        right_max[-1] = -1
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])

        ans = 0
        for i in range(1, len(height) - 1):
            if height[i] < min(left_max[i], right_max[i]):
                ans += min(left_max[i], right_max[i]) - height[i]
        return ans


def test_solution(subtests):
    with subtests.test("Example 1"):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        assert Solution().trap(height) == 6
    with subtests.test("Example 2"):
        height = [4, 2, 0, 3, 2, 5]
        assert Solution().trap(height) == 9

```

---

> [!info] Keywords
> - ...

> [!tip] Refs
> - LeetCode :: [42. trapping-rain-water](https://leetcode.com/problems/trapping-rain-water)
> - GitHub :: [algorithm-ps/leetcode/42-trapping-rain-water](https://github.com/nno0obb/algorithm-ps/tree/main/leetcode/42-trapping-rain-water)

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
