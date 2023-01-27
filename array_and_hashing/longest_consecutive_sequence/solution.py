from collections import defaultdict
class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (len(nums) == 0):
      return 0

    d = dict.fromkeys(nums, False)
    ranges = defaultdict(int)
    res = 1
    for key in d.keys():
      ranges[key] = 1

    for num in d.keys():
      # if not visited
      if (not d[num]):
        d[num] = True # mark as visited
        tmp = num
        while (d.get(tmp-1) != None):
          d[tmp-1] = True
          ranges[num] = ranges[num] + ranges[tmp-1]
          res = max (ranges[num], res)
          if (ranges[tmp-1] > 1):
            break
          tmp = tmp - 1
      else:
        pass
    
    return res