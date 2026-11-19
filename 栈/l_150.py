from typing import List

def solve(exprs:List[str]):

    for case in exprs:
        output = infix_to_post(case)
        print(f"output:{output}")
        res = cal(output)
        print(f"res:{res}")

def infix_to_post(expr:str):

    output = []
    op_stack = []

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 0,
    }

    for ch in expr:
        if ch == ' ':
            continue
        if ch.isdigit():
            output.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()
        else:
            # 优先级高的在靠左边
            while op_stack and precedence[op_stack[-1]] >= precedence[ch]:
                output.append(op_stack.pop())
            op_stack.append(ch)

    while op_stack:
        output.append(op_stack.pop())

    return output

def cal(expr:str):

    st = []

    for ch in expr:
        if ch.isdigit():
            st.append(int(ch))
        else:
            if ch == '+':
                st.append(st.pop() + st.pop())
            elif ch == '-':
                st.append(st.pop() - st.pop())
            elif ch == '*':
                st.append(st.pop() * st.pop())
            else:
                st.append(st.pop() * st.pop())

    return st[0]

if __name__ == "__main__":

    cases = ["1 * (2 + 3)",
             "2 * (3 + 6)",
             "(1 + 2) * 3", 
             "1 + 2 * 3"]

    solve(cases)