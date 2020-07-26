def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i > 1 and nums[i] == nums[i - 1]:
            continue
        d = {}
        for x in nums[i + 1:]:
            if x not in d:
                d[-v - x] = 1
            else:
                res.add((v, -v - x, x))

    return map(list, res)


map = three_sum([-1, 0, 1, -3, 0, 3])
print(map)
