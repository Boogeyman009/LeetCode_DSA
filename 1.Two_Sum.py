class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in ans:
                return [ans[k],i]
            ans[nums[i]] = i