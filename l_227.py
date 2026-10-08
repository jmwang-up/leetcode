from typing import List

class Solution:
    def calculate(self, s: str) -> int:

        def tokenize(s:str):
            operators = "+-*/()"
            result = ''
            for ch in s:
                if ch in operators:
                    result += " " + ch + " "
                elif ch.isdigit():
                    result += ch
            return result.split()

        def infix_to_post(s:List[str]) -> str:

            precedence = {
                '+': 1,
                '-': 1,
                '(': 0,
                "*": 2,
                "/": 2,
                'neg':3
            }

            output = []
            op_stack = []

            for i in range(len(s)):
                c = s[i]
                # print(f"output:{output} -> op_stack:{op_stack}")
                if c.isdigit():
                    output.append(c)
                elif c == '(':
                    op_stack.append(c)
                elif c == ')':
                    while op_stack and op_stack[-1] != '(':
                        output.append(op_stack.pop())
                    # 弹出)
                    op_stack.pop()
                else:
                    # 说明第一个字符就是+ 或者 -, 按照单元运算符处理
                    if i == 0:
                        op_stack.append('neg')
                        continue
                    # 需要判断是否是单元运算符
                    if i >= 0:
                        # 不是数字, 说明是单元运算符
                        if not s[i - 1].isdigit() and s[i - 1] != ')':
                            c = 'neg'
                    # 如果左边不是数字，即为单元运算符
                    while op_stack and precedence[op_stack[-1]] >= precedence[c]:
                        output.append(op_stack.pop())
                    op_stack.append(c)
            # print(f"output:{output} -> op_stack:{op_stack}")
            while op_stack:
                output.append(op_stack.pop())
            return output


        def cal(exprs:List[str]):

            st = []
            op_to_binary_fn = {
                '+': lambda x,y:x+y,
                '-': lambda x,y: x - y,
                '*': lambda x,y:x * y,
                '/': lambda x,y: int(x/y)
            }

            for ch in exprs:
                if ch.isdigit():
                    st.append(int(ch))
                elif ch in '+-*/':
                    num2 = st.pop()
                    num1 = st.pop()
                    num = op_to_binary_fn[ch](num1, num2)
                    st.append(num)
                else:
                    num1 = st.pop()
                    num = 0 - num1
                    st.append(num)
            # print(st)
            return ''.join(list(map(str, st)))
        
        token = tokenize(s)
        print(f"token:{token}")
        post = infix_to_post(token)
        print(f"post:{post}")
        return int(cal(post))


if __name__ == "__main__":

    so = Solution()
    cases = ["1-(     -2)", "(1+(4+5+2)-3)+(6+8)", "1-11", "- (3 + (4 + 5))", "3+2*2"]
    for case in cases:
        res = so.calculate(case)
        print(res)