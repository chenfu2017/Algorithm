class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d ={}
        result ={}
        found=0
        if len(nums)>=4:
            for i in range (len(nums)-1):
                    for j in range (i+1, len (nums)):
                        s=nums[i]+nums[j]
                        if d.get(s)==None:
                            d[s]=[]
                        d[s].append([i,j])
        for i in d:
            if d.get(target-i)!=None:
                for j in d[i]:
                    for k in d[target-i]:
                        if j[0]!=k[0] and j[1]!=k[1] and j[1]!=k[0] and j[0]!=k[1]:
                            tk = j + k
                            tk = [nums[i] for i in tk]
                            tk.sort()
                            result[tuple(tk)] = 1
                found = 1
        if found == 0 or len(nums) < 4:
            return []
        return (list(result.keys()))


nums = [1, 0, -1, 0, -2, 2]
print(Solution().fourSum(nums,0))
