class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex +=1
        last_arr=[0]*rowIndex
        curr_arr=[0]*rowIndex
        last_arr[0]=1
        for i in range(rowIndex):
            for j in range(i+1):
                if j == 0 or j == i:
                    curr_arr[j]=1
                else :
                    curr_arr[j]= last_arr[j-1]+last_arr[j]
            last_arr[0:i+1] = curr_arr[0:i+1]
        return curr_arr

print(Solution().getRow(1))