class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        ###############
        if len(self.p) != len(self.p):
            return False
        if '.*' in self.p:
            return True
        elif "*" in self.p:
            if len(self.s) != len(self.p):
                return False
            else:
                for chr in self.s:
                    if self.p[0] != chr:
                        return False
                return True
        ###############
        elif '.' in self.p:
            if len(self.p) != len(self.p):
                return False
            else:
                if self.s[1] == self.p[1]:
                    return True
                elif self.s[0] == self.p[0]:
                    return True
                else:
                    return False
        elif self.s in self.p:
            return True

getAnsw = Solution()
print(getAnsw.isMatch("aa", "a"))