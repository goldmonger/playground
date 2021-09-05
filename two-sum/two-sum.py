class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            #print(comp)
            if comp in mydict.keys():
                return(i, mydict[comp])
            else:
                mydict[nums[i]] = i
                #print (mydict)