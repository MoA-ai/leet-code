class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from queue import PriorityQueue

        p_que = PriorityQueue()
        for num in nums:
            p_que.put(-num)

        for idx in range(k):
            kth_val = p_que.get()

        return -kth_val
