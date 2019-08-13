class Solution:
    def rotatedDigits(self, N: int) -> int:
        total = 0
        contain_347 = set(["3","4","7"])
        only_018 = set(["0","1","8"])
        
        for n in range(1, N + 1):
            n = set(list(str(n)))
            if n.intersection(contain_347) or n.issubset(only_018):
                continue
            total += 1
            
        return total