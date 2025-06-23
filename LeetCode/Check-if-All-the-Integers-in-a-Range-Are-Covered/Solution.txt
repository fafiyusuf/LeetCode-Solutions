class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        allNum = []
        for start, end in ranges:
            for num in range(start , end + 1 ):
                allNum.append(num)
        for number in range(left , right+1):
            if number  not in allNum:
                return False
        return True

        