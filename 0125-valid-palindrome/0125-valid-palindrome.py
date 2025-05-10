class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []
        for c in s:
            if c.isalnum():
                newlist.append(c.lower())
        return newlist == newlist[::-1]