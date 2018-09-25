class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic ={}
        re=[]
        for n in nums:
            if n not in dic:
                dic[n]=0
            dic[n]+=1

        if 0 in dic and dic[0] > 2:
            re.append([0, 0, 0])

            # Check for positives and negatives
        pos = [p for p in dic if p > 0]
        neg = [n for n in dic if n < 0]

        for p in pos:
            for n in neg:
                rem = - (p + n)
                if rem not in dic.keys(): continue

                if rem == p and dic[p] > 1:
                    re.append([n, p, rem])
                elif rem == n and dic[n] > 1:
                    re.append([n, rem, p])
                elif rem < p and rem > n:
                    re.append([n, rem, p])

        return re



nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
