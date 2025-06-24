from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic1 = {}
        for i, num in enumerate(nums):
            if num in dic1:
                dic1[num].append(i)
            else:
                dic1[num] = [i]

        count = 0
        for indices in dic1.values():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count
