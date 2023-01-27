from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: List[int]
      """
      counts = Counter(nums)
      sorted_frequency = sorted(counts, key=lambda num: counts[num], reverse=True)
      return sorted_frequency[:k]
      
      