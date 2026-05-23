class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = False
        if len(s1) < 1 or len(s2) < 1:
            return perm
        
        count = defaultdict(int)
        count_t = defaultdict(int)
        for char in s1:
            count_t[char] += 1
        k = len(s1)
        l = 0
        for r in range(len(s2)):
            count[s2[r]] += 1

            while (r-l+1) > k:
                
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1 
            if count_t == count:
                return True

            
        return True if count_t == count else False
            
