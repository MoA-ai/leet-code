class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1

        while s != e:
            mid = int((s + e) / 2)
            if target <= nums[mid]:
                e = mid
            else:
                s = mid + 1
            print(s, e)
        # return s
        return s+1 if nums[s] < target else s
        # return s if nums[s] == target else s + 1