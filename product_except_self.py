def productExceptSelf(self, nums: List[int]) -> List[int]:
    # TWO PASS
    # # The length of the input array 
    # length = len(nums)
    
    # # The answer array to be returned
    # answer = [0]*length
    
    # # answer[i] contains the product of all the elements to the left
    # # Note: for the element at index '0', there are no elements to the left,
    # # so the answer[0] would be 1
    # answer[0] = 1
    # for i in range(1, length):
    #     # answer[i - 1] already contains the product of elements to the left of 'i - 1'
    #     # Simply multiplying it with nums[i - 1] would give the product of all 
    #     # elements to the left of index 'i'
    #     answer[i] = nums[i - 1] * answer[i - 1]
    
    # # R contains the product of all the elements to the right
    # # Note: for the element at index 'length - 1', there are no elements to the right,
    # # so the R would be 1
    # R = 1;
    # for i in reversed(range(length)):
    #     # For the index 'i', R would contain the 
    #     # product of all elements to the right. We update R accordingly
    #     answer[i] *= R
    #     R *= nums[i]
    
    # return answer

    # ONE PASS
    # n = len(nums)
#     res = [1] * n
#     l = r = 1
#     i = 0
#     while i < n:
#         res[i] *= l
#         l *= nums[i]
#         i += 1
#         res[n - i] *= r
#         r *= nums[n - i]
#     return res

    # ONE PASS PYTHONIC
    n = len(nums)
    res = [1] * n         
    r = l = 1        
    for i, j in zip(range(n), reversed(range(n))):
        res[i] *= l
        l *= nums[i]
        
        res[j] *= r
        r *= nums[j]
        
    return res