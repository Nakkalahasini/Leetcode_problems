class Solution:
    def jump(self, nums: List[int]) -> int:
        ce=0
        ml=0
        jump=0
        n=len(nums)
        for i in range(n-1):
            ml=max(ml,i+nums[i])
            if i==ce:
                jump+=1
                ce=ml
        return jump
        
