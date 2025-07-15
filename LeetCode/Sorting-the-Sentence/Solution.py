class Solution:
    def sortSentence(self, s: str) -> str:
        def isnumber(word):
            number=''
            for char in word:
                if char.isdigit():
                    number += char
            return number
        array = s.split()
        sorted_array = sorted(array , key=isnumber)
        result = []
        for i in sorted_array:
            x = i[:-1]
            result.append(x)
        result = ' '.join(result)
        return result
        