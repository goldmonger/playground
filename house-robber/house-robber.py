class Solution:
    def rob(self, nums: List[int]) -> int:
        loot = 0
        skip = 0
        for i in range(len(nums)):
            temp = skip
            
            skip = max(temp, loot)
            loot = nums[i] + temp
        #print(loot)
        #print(skip)
        return(max(loot,skip))
            
            