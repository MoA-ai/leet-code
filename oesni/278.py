class Solution:
    def firstBadVersion(self, n: int) -> int:
        s = 0
        e = n

        while s != e:
            mid = int((s + e) / 2)
            if isBadVersion(mid):
                e = mid
            else:
                s = mid + 1

        return s