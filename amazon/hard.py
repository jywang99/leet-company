from typing import List


class WordBreak2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = { len(s): [""] }

        def recurse(i: int) -> List[str]:
            if i in dp:
                return dp[i]

            rs = []
            for word in wordDict:
                if s[i:].startswith(word):
                    for suf in recurse(i + len(word)):
                        rs.append((word + " " + suf).strip())

            dp[i] = rs
            return rs
        
        return recurse(0)

