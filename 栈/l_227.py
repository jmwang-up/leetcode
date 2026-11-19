from typing import List

class Solution:
    def calculate(self, s: str) -> int:

        def tokenizer(s):
            tokens = ''
            for c in s:
                if c in "+-*/()":
                    tokens += " " + c + " "
                else:
                    tokens += c
            return tokens.split()


        def midfixtopost(s:List[str]):

            output = []
            op_stack = []

            precedence = {
                "+":1,
                "-":1,
                "*":2,
                "/":2,
                "neg":3,
                "(": -1
            }

            for i in range(len(s)):

                c = s[i]
                if c.isdigit():
                    output.append(c)
                elif c == '(':
                    op_stack.append(c)
                elif c == ')':
                    while op_stack and op_stack[-1] != '(':
                        output.append(op_stack.pop())
                    op_stack.pop()
                else:
                    if i == 0:
                        op_stack.append('neg')
                        continue
                    if not s[i - 1].isdigit() and s[i - 1] != ')':
                        c = 'neg'

                    while op_stack and precedence[op_stack[-1]] >= precedence[c]:
                        output.append(op_stack.pop())
                    op_stack.append(c)

            print(f"output{output}, op_stack:{op_stack}")
            while op_stack:
                output.append(op_stack.pop())
            return output


        def cal(s:List[str]):

            st = []

            operator_func = {
                "+": lambda x,y: x + y,
                '-': lambda x,y: x - y,
                '*': lambda x,y: x * y,
                '/': lambda x,y: int(x / y),
                'neg': lambda x:0 - x
            }

            for c in s:
                if c.isdigit():
                    st.append(int(c))
                elif c == 'neg':
                    st.append(operator_func[c](st.pop()))
                else:
                    a = st.pop()
                    b = st.pop()
                    st.append(operator_func[c](b, a))
            return st[-1]

                
        tokens = tokenizer(s)
        print(f"tokens:{tokens}")
        post = midfixtopost(tokens)
        print(f"post:{post}")
        res = cal(post)
        return res

    


        
if __name__ == "__main__":

    so = Solution()
    cases = ["1-(     -2)", "(1+(4+5+2)-3)+(6+8)", "1-11", "- (3 + (4 + 5))", "3+2*2"]
    for case in cases:
        res = so.calculate(case)
        print(res)