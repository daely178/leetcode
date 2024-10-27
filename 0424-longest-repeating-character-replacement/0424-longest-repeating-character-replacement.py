class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start = 0
        freq = defaultdict(int)
        max_freq = 0
        longest = 0

        for e in range(len(s)):
            freq[s[e]] = freq[s[e]] + 1
            max_freq = max(max_freq, freq[s[e]])

            if (e-start+1-max_freq) > k: # valid check
                freq[s[start]] -= 1
                start += 1
            else:
                longest = e-start+1

            # AABABBA
            #longest = e-start+1
            #longest = max(longest, (e-start+1))

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