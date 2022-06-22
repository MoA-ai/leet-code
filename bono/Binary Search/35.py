class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first_idx = 0
        last_idx = len(nums) - 1

        target_idx = 0
        while first_idx <= last_idx:
            middle_idx = (first_idx + last_idx) // 2

            if nums[middle_idx] == target:
                return middle_idx

            if nums[middle_idx] < target:
                first_idx = middle_idx + 1

            else:
                last_idx = middle_idx - 1

        return first_idx
