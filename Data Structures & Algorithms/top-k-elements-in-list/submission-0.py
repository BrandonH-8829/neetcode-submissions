class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countN = {}
        fin = [] * k
        for i in range(len(nums)):
            countN[nums[i]] = 1 + countN.get(nums[i], 0)
            #countS[s[i]] = 1 + countS.get(s[i], 0)
        
        countN = dict(sorted(countN.items(), key=lambda item: item[1], reverse=True))

        for i, v in enumerate(countN):
            if k == i:
                return fin
            fin.append(v)

        return fin