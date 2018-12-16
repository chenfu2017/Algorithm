class Solution:
    list = []

    m = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def find_combinations(self, digits, index, s):
        if index == len(digits):
            self.list.append(s)
            return

        c = digits[index]
        chars = self.m.get(c)
        for char in chars:
            self.find_combinations(digits, index + 1, s + char)
        return

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if (digits == ""):
            return []
        self.list.clear()
        self.find_combinations(digits, 0, '')
        print(self.list)
        return self.list


Solution().letterCombinations('2')
