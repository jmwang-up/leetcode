class Solution:
    def isValid(self, s: str) -> bool:
        
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


if __name__ == "__main__":

    so = Solution()
    for case in ["()[]{}", "([)]", '(]']:
        print(so.isValid(case))