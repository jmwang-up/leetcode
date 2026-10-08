class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        ans = []

        def isValid(s: str) -> bool:
                
            stack = []
    
            mapping = {
                "]":"[",
                ")":"(",
                "}":"{"
            }
    
            for c in s:
                # print(f"stack:{stack}")
                if stack and c in mapping:
                    if stack[-1] != mapping.get(c):
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(c)
            return not stack
        

        def back_strace(path):

            if len(path) == 6:
                if isValid(path):
                    ans.append(path)
                return
            back_strace(path + "(")
            back_strace(path + ")")

        back_strace("")

        return ans

if __name__ == "__main__":

    so = Solution()
    so.generateParenthesis(3)