class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        middle_len = len(s) // 2
        for idx in range(middle_len):
            s[idx], s[-1 - idx] = s[-1 - idx], s[idx]
