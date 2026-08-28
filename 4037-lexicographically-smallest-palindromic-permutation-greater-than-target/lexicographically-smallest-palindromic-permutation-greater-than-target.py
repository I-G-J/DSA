from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        odds = ''.join(c for c in counts if counts[c]&1)
        if len(odds) > 1:
            return ''
        for c in counts:
            counts[c] //= 2
        res = ''
        def backtrack(i, curr, t):
            nonlocal res
            if i == len(s)//2:
                cand = curr + odds + curr[::-1]
                if cand > target:
                    res = cand
                return
            for c in sorted(counts):
                if counts[c] == 0:
                    continue
                if t and c < target[i]:
                    continue
                counts[c] -= 1
                backtrack(i+1, curr+c, t and c == target[i])
                counts[c] += 1
                if res != '':
                    return
        backtrack(0, '', True)
        return res