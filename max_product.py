def maxProduct(self, nums: List[int]) -> int:
    res = nums[0]
    l = r = 0
    for l_num, r_num in zip(nums, reversed(nums)):
        l = (l or 1) * l_num
        r = (r or 1) * r_num
        res = max(res, l, r)
    
    return res