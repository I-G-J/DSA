class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        first=list(s)
        second=list(t)
        first.sort()
        second.sort()
    
        for i in range(len(first)):
            if first[i]!=second[i]:
                return False
        return True