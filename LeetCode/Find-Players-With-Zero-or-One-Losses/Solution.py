from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)
        lose = defaultdict(int)
        for a, b in matches:
            win[a]+=1
            lose[b]+=1
        never_lost=[i for i in win if i not in lose]
        lost_once = [i for i ,count in lose.items() if count == 1]
        return [sorted(never_lost), sorted(lost_once)]