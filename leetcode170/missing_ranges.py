# https://leetcode.com/problems/missing-ranges/

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        if len(nums) == 0:
            if upper == lower:
                return [f"{upper}"]
            else:
                return [f"{lower}->{upper}"]
        pre,post, output = None,None,[]
        if lower < nums[0]-1:
            pre = f"{lower}->{nums[0]-1}"
        elif lower == nums[0]-1:
            pre = f"{lower}"
            
        if nums[-1] == upper-1:
            post = f"{upper}"
        elif nums[-1] < upper-1:
            post = f"{nums[-1]+1}->{upper}"
        
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i] + 1:
                continue
            elif nums[i+1] == nums[i]+2:
                output.append(f"{nums[i]+1}")
            else:
                output.append(f"{nums[i]+1}->{nums[i+1]-1}")
        if post:
            output.append(post)
        if pre:
            return [pre,*output]
        else:
            return output