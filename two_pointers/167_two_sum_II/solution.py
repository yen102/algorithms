from helper import Helper

class Solution(object):
  helper = Helper()
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(numbers)):
      j = self.helper.binary_search(numbers, i+1, len(numbers)-1, target - numbers[i])
      if (j != -1):
        return [i+1, j+1]
    return [-1, -1]

    

solution = Solution()
solution.twoSum([5,25,75], 100)