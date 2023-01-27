from solution import Solution
class TestSolution:
  solution = Solution()
  def test_1(self):
    numbers = [2,7,11,15]
    target = 9

    assert self.solution.twoSum(numbers=numbers, target=target) == [1,2]

  def test_2(self):
    numbers = [2,3,4]
    target = 6

    assert self.solution.twoSum(numbers=numbers, target=target) == [1,3]
  
  def test_3(self):
    numbers = [-1,0]
    target = -1

    assert self.solution.twoSum(numbers=numbers, target=target) == [1,2]

  def test_4(self):
    numbers = [0,0,3,4]
    target = 0

    assert self.solution.twoSum(numbers=numbers, target=target) == [1,2]
    
    