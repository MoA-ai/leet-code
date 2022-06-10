class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1

        while s != e:
            mid = int((s+e)/2)
            num_mid = nums[mid]
            if target <= num_mid:
                e = mid
            elif target > num_mid:
                s = mid + 1

        return s if nums[s] == target else -1