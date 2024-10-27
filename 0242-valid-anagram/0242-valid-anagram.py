class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        for c in s:
            freq_s[c] += 1
        for c in t:
            freq_t[c] += 1
        
        return freq_s == freq_t