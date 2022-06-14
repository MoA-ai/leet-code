class Solution:
    def climbStairs(self, n: int) -> int:
        """
        to "N"
        (N-1) 에서 1칸 이동
        (N-2) 에서 2칸 이동
        """
        c = [-1] * 46
        c[0] = 0
        c[1] = 1
        c[2] = 2

        def climb_recursion(c, n: int) -> int:
            if n < 0:
                return 0
            if c[n] > 0:
                return c[n]
            c[n] = climb_recursion(c, n-1) + climb_recursion(c, n-2)
            return c[n]

        val = climb_recursion(c, n)
        return val