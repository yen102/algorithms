from helper import Helper

class TestUtils(object):
  helper = Helper()
  def test_1(self):
    numbers = [1, 2, 3]
    target = 2
    start = 0
    end = 2
    assert self.helper.binary_search(numbers, start, end, target) == 1
  

  def test_2(self):
    numbers = [1, 2, 3]
    target = 4
    start = 0
    end = 2
    assert self.helper.binary_search(numbers, start, end, target) == -1

  def test_3(self):
    numbers = [1]
    target = 1
    start = 0
    end = 0
    assert self.helper.binary_search(numbers, start, end, target) == 0
  
  def test_4(self):
    numbers = [1]
    target = 0
    start = 0
    end = 0
    assert self.helper.binary_search(numbers, start, end, target) == -1
  
  def test_5(self):
    numbers = [1, 2, 3, 4, 5, 6]
    target = 4
    start = 2
    end = 5
    assert self.helper.binary_search(numbers, start, end, target) == 3

