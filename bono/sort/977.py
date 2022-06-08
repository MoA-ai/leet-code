class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_idx = 0
        len_nums = len(nums)
        for fast_idx in range(len_nums):
            if nums[slow_idx] == 0 and nums[fast_idx] != 0:
                nums[slow_idx], nums[fast_idx] = nums[fast_idx], nums[slow_idx]

            if nums[slow_idx] != 0:
                slow_idx += 1
