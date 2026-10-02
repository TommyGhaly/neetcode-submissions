class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        c1 = 0
        max_l = 0
        for c2 in range(len(s)):
            while s[c2] in visited:
                visited.remove(s[c1])
                c1 += 1
            visited.add(s[c2])
            max_l = max(max_l, c2 - c1 + 1)
        return max_l