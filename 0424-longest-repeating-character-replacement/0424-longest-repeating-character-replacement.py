class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start, longest, maxfreq = 0,0,0
        freq = defaultdict(int)

        for i in range(len(s)):
            freq[s[i]] += 1
            maxfreq = max(maxfreq, freq[s[i]])
            window = i-start+1

            if (window-maxfreq) > k:
                freq[s[start]] -= 1
                start += 1
            else:
                longest = window
        return longest

'''
brute force
- dictionary
- remove longest
- count and upate

sliding window

    A A B A B B A
      s
            e

k + max freq = window = 5
k=1
dict A:2 B:2

'''        