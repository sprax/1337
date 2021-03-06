class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._sum_up_to = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            self._sum_up_to[i] = self._sum_up_to[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum_up_to[j+1] - self._sum_up_to[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

