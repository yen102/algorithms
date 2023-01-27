from solution import Solution
class TestSolution(object):
  sol = Solution()
  def test_1(self):
    height = [1,8,6,2,5,4,8,3,7]
    assert self.sol.maxArea(height) == 49

  def test_2(self):
    height = [8,6,2,5,4,8,3,7]
    assert self.sol.maxArea(height) == 49
  
  def test_3(self):
    height = [8,6]
    assert self.sol.maxArea(height) == 6