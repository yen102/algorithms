from solution import Solution

class TestSolution:
  def test_1(self):
    nums = [1,1,1,2,2,3]
    k = 2
    solution = Solution()
    assert solution.topKFrequent(nums=nums, k=k) == [1,2]
  def test_2(self):
    nums = [1]
    k = 1
    solution = Solution()
    assert solution.topKFrequent(nums=nums, k=k) == [1]