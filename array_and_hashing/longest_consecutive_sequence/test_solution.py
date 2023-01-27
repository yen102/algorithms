from solution import Solution

class TestSolution:
  solution = Solution()

  def test_1(self):
    nums = [100,4,200,1,3,2]
    assert self.solution.longestConsecutive(nums=nums) == 4
  
  def test_2(self):
    nums = [0,3,7,2,5,8,4,6,0,1]
    assert self.solution.longestConsecutive(nums=nums) == 9
  
  def test_3(self):
    nums = []
    assert self.solution.longestConsecutive(nums=nums) == 0
  
  def test_4(self):
    nums = [100,101,5,1,2,4,6,200]
    assert self.solution.longestConsecutive(nums=nums) == 3
  
  def test_5(self):
    nums = [100,101,5,1,2,4,6,200,3]
    assert self.solution.longestConsecutive(nums=nums) == 6