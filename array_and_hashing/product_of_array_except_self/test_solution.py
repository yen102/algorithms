from solution import Solution

class TestSolution:
  def test_1(self):
    nums = [-1,1,0,-3,3]
    solution = Solution()
    assert solution.productExceptSelf(nums=nums) == [0,0,9,0,0]

  def test_2(self):
    nums = [-1, 0]
    solution = Solution()
    assert solution.productExceptSelf(nums=nums) == [0, -1]

  def test_3(self):
    nums = [1,2,3,4]
    solution = Solution()
    assert solution.productExceptSelf(nums=nums) == [24,12,8,6]