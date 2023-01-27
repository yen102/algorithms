class Helper(object):
  def binary_search(self, numbers, start, end, target):
    mid = (start + end) // 2
    if (mid > end or mid < start): 
      return -1
    if (numbers[mid] == target):
      return mid
    elif (numbers[mid] < target):
      return self.binary_search(numbers, mid + 1, end, target)
    else:
      return self.binary_search(numbers, start, mid-1, target)
    