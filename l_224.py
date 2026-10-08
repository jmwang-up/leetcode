from typing import List

class Solution:
    def calculate(self, s: str) -> int:

        # 1. 词法分析
        operators = "+-*/()"
        def tokenize(s:str):

            tokens = ''
            for ch in s:
                if ch in operators:
                    tokens += " " + ch + " "
                elif ch.isdigit():
                    tokens += ch
            return tokens.split()

        # 2. 中缀转后缀
        def midfixtopost(tokens:List[str]):

            output = []
            op_stack = []

            precedence = {
                "*":2,
                "/":2,
                "+":1,
                "-":1,
                "(":0,
                "neg":3
            }

            # for ch in tokens:
            for i in range(len(tokens)):
                ch = tokens[i]
                if ch.isdigit():
                    output.append(ch)
                elif ch == '(':
                    op_stack.append(ch)
                elif ch == ')':
                    while op_stack and op_stack[-1] != '(':
                        output.append(op_stack.pop())
                    # 弹出左括号
                    op_stack.pop()
                else:
                    if i == 0:
                        op_stack.append("neg")
                        continue
                    if not tokens[i - 1].isdigit() and tokens[i - 1] != ')':
                        ch = 'neg'
                    while op_stack and precedence[op_stack[-1]] >= precedence[ch]:
                        output.append(op_stack.pop())
                    op_stack.append(ch)

            while op_stack:
                output.append(op_stack.pop())
            return output

        # 3. 根据后缀表达式计算
        def calculate(s:str):
            
            st = []
            for ch in s:
                if ch.isdigit():
                    st.append(int(ch))
                elif ch == '+':
                    a = st.pop()
                    b = st.pop()
                    st.append(b + a)
                elif ch == '-':
                    a = st.pop()
                    b = st.pop()
                    st.append(b - a)
                elif ch == "*":
                    a = st.pop()
                    b = st.pop()
                    st.append(b * a)
                elif ch == '/':
                    a = st.pop()
                    b = st.pop()
                    st.append(int(b/a))
                else:
                    st.append(0 - st.pop())

            return st[0]

        tokens = tokenize(s)
        print(f"tokens:{tokens}")
        post = midfixtopost(tokens)
        print(f"post:{post}")
        res = calculate(post)
        return res


if __name__ == "__main__":

    so = Solution()
    cases = ["3+2*2", " 3/2 ", " 3+5 / 2 "]
    for case in cases:
        print(so.calculate(case))