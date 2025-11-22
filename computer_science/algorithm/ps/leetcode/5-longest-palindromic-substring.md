---
created_at: 2025/06/20 22:36:06
updated_at: 2025/06/20 22:36:34
---
---

```python
"""
# 리트코드
# No. 5 / longest-palindromic-substring
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        # 홀수 길이
        for i in range(len(s)):
            for j in range(0, min(i + 1, len(s) - i)):
                if s[i - j] == s[i + j]:
                    if len(ans) < 2 * j + 1:
                        ans = s[i - j : i + j + 1]
                else:
                    break
        # 짝수 길이
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                for j in range(0, min(i + 1, len(s) - i - 1)):
                    if s[i - j] == s[i + j + 1]:
                        if len(ans) < 2 * j + 2:
                            ans = s[i - j : i + j + 2]
                    else:
                        break
        return ans


def test_solution(subtests):
    with subtests.test("Example 1"):
        s = "babad"
        output = "bab"
        assert Solution().longestPalindrome(s) in [output, "aba"]
    with subtests.test("Example 2"):
        s = "cbbd"
        output = "bb"
        assert Solution().longestPalindrome(s) == output
    with subtests.test("Example 3"):
        s = "a"
        output = "a"
        assert Solution().longestPalindrome(s) == output

```

---

> [!info] Keywords
> - ...

> [!tip] Refs
> - LeetCode :: [5. longest-palindromic-substring](https://leetcode.com/problems/longest-palindromic-substring)
> - GitHub :: [algorithm-ps/leetcode/5-longest-palindromic-substring](https://github.com/nno0obb/algorithm-ps/tree/main/leetcode/5-longest-palindromic-substring)

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
