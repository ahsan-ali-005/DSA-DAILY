class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(" , "}" : "{" , "]" : "["}

        for ch in s:
            if ch in hashmap:
                if stack and stack[-1] == hashmap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False

ob = Solution()
print(ob.isValid("(){[]}"))

# Output
# True