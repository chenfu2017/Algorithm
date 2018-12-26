class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in h:
                h[key].append(s)
            else:
                h[key] = [s]

        return list(h.values())

strs=["hos","bbo","bob"]
print(Solution().groupAnagrams(strs))