import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[-1] * nums[i - 1])


        suffix = []
        for j in range(len(nums) - 1 , -1 , -1): 
            if j == len(nums) - 1 : 
                suffix.append(1)
            else :
                suffix.append(suffix[-1] * nums[j + 1])
        suffix.reverse()

    
        result = []
        for k in range(len(prefix)) : 
              result.append(prefix[k] * suffix[k])

        return result
                