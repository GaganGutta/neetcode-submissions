class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted(s)
        sorted(t)
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        if s == t:
            return True
        else:
            return False
