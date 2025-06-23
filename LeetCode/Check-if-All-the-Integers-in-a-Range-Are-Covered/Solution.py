class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      numbers=[]
      for start , end in ranges:
        for i in range (start , end+1):
            numbers.append(i)
      for num in range(left , right + 1):
        if num not in numbers:
            return False
      return True