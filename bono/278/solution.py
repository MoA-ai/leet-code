# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        first_idx = 1
        last_idx = n

        first_bad_version = 0
        while first_idx <= last_idx:
            middle_idx = (first_idx + last_idx) // 2

            if isBadVersion(middle_idx):
                # True
                last_idx = middle_idx - 1
                first_bad_version = middle_idx
            else:
                # False
                first_idx = middle_idx + 1

        return first_bad_version
