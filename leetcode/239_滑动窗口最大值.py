def maxSlidngWindowl(nums, k):
    if not nums: return []
    window, res = [], []
    for i, x in enumerate(nums):
        print(i,x)
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and nums[window[-1]] < x:
            window.pop(-1)
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res

# 每相邻3个元素里面 最大的元素
res = maxSlidngWindowl([1, 3, -1, -3, 5, 3, 6], 3)
print(res)
