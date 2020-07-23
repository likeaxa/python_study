# https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
# leelcode 地址
from typing import List


def maxSubArray(self, nums: List[int]) -> int:
    maxVal = nums[0]
    i = 1
    while i < len(nums):
        cur = nums[i]
        maxVal = m0ax(cur + maxVal, cur)
    return maxVal


print(maxSubArray(1, [1, 2]))
