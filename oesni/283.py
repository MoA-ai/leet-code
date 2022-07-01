class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeros = [x for x in nums if x != 0]
        nums[:] = non_zeros + [0] * (len(nums) - len(non_zeros))