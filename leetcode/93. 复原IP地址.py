class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        r = []
        self.dfs(0, '', s,r)
        # print(r)
        return r

    def dfs(self, count, ip, s,r):
        if count == 4:
            if s == '':
                r.append(ip[:-1])
            return
        if len(s) > 0:
            self.dfs(count + 1, ip + s[0] + '.', s[1:],r)
        if len(s) > 1 and s[0] != '0':
            self.dfs(count + 1, ip + s[0:2] + '.', s[2:],r)
        if len(s) > 2 and s[0] != '0' and int(s[0:3]) < 256:
            self.dfs(count + 1, ip + s[0:3] + '.', s[3:],r)


s = "25525511135"
Solution().restoreIpAddresses(s)