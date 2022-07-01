class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        mask = [2**x for x in range(33)]
        return sum([1 if (n & m > 0) else 0 for m in mask]) == 1