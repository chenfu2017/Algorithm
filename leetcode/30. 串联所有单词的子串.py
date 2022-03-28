from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m = {}
        if len(words) == 0:
            return []
        one_word_len = len(words[0])
        word_count = len(words)
        for word in words:
            if word in m:
                m[word] += 1
            else:
                m[word] = 1
        words_len = one_word_len * word_count
        end = len(s) - words_len + 1
        ans = []
        for i in range(end):
            substr = s[i:i + words_len]
            cur_map = m.copy()
            for j in range(0, words_len, one_word_len):
                cur = substr[j:j + one_word_len]
                if cur not in cur_map or cur_map[cur] == 0:
                    break
                else:
                    if cur_map[cur] == 1:
                        cur_map.pop(cur)
                    else:
                        cur_map[cur] -= 1
                if len(cur_map) == 0:
                    ans.append(i)
        # print(ans)
        return ans



s = "barfoothefoobarman"
words = ["foo", "bar"]
Solution().findSubstring(s, words)
