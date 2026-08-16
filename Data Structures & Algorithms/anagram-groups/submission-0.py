class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)
        res = []

        for s in strs:
            # keys in maps must be immutable
            sorted_s = "".join(sorted(s))
            
            # sorted string is the key to the strings as values
            anagram_map[sorted_s].append(s)

        # loop over the organized strings (values in anagram_map)
        for val in anagram_map.values():
            res.append(val)

        return res

        