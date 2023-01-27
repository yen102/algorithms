class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    length = len(nums)
    left_products = [1] * length
    right_products = [1] * length
    res = [1] * length
    for i in range(1, length):
      left_products[i] = left_products[i-1] * nums[i-1]
    
    for i in range(length-2, -1, -1):
      right_products[i] = right_products[i+1] * nums[i+1]

    for i in range(length):
      res[i] = left_products[i] * right_products[i]
    
    return res
