# Solution A
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            mp[key].append(st)

        return list(mp.values())


# Solution B
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            ct = [0] * 26
            for ch in st:
                ct[ord(ch) - ord('a')] += 1
            mp[tuple(ct)].append(st)
        return list(mp.values())
