class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        sett = set() # to manage the duplicate chars
        length = 0
        
        # will keep a window of size (right - left + 1)
        for right in range(len(s)):
            # if you encounter a duplicate (already in sett); while for moving >= once
            while s[right] in sett:
                # shift over left pointer
                sett.remove(s[left])
                left += 1

            sett.add(s[right])
            length = (right - left) + 1

            longest = max(longest, length)
        
        return longest
