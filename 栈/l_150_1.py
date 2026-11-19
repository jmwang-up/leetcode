from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []
        operate_func = {
            "+" : lambda x,y:x+y,
            '-': lambda x,y:x-y,
            '*': lambda x,y:x*y,
            '/': lambda x,y:int(x/y)
        }

        for ch in tokens:
            if ch not in "+-*/":
                st.append(int(ch))
            else:
                a = st.pop()
                b = st.pop()
                st.append(operate_func[ch](b,a))

        return st[-1]



if __name__ == "__main__":
    so = Solution()
    res = so.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(f"res:{res}")