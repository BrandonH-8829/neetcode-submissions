class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_sub = 1
        l, r = 0, 1
        current_array = [s[0]]

        while l < len(s) and r < len(s):
            if s[r] not in current_array:
                current_array.append(s[r])
            else:
                l += 1
                r = l
                current_array = [s[l]]
            max_sub = max(len(current_array), max_sub)
            r += 1
        return max_sub