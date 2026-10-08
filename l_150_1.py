from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for ch in tokens:
            print(st)
            if ch == '+':
                a = st.pop()
                b = st.pop()
                st.append(a + b)
            elif ch == '-':
                a = st.pop()
                b = st.pop()
                st.append(b - a)
            elif ch == '*':
                a = st.pop()
                b = st.pop()
                st.append(a * b)
            elif ch == '/':
                a = st.pop()
                b = st.pop()
                st.append(int(b/a))
            else:
                st.append(int(ch))
            

        return st[0]



if __name__ == "__main__":
    so = Solution()
    res = so.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(f"res:{res}")