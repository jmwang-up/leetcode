import sys

"""
一、题目要求
给定一个由 0 1 ! & | ( ) 组成的字符串，例如 !(1&0)|0&1，要求计算出它的逻辑值（0 或 1）。
运算符：
! 逻辑非（一元）
& 逻辑与
| 逻辑或
优先级：! > & > |，( 最低但起分组作用
"""
def tokenize(s:str):
    """
    词法分析
    """
    tokens = ''
    for ch in s:
        if ch in '01!&|()':
            tokens += ch

    return tokens

def midfixtopost(s:str):
    """
    中缀转后缀
    1 + 2 * 3 -> 1 2 3 * + 
    """
    """
    申请一个存储操作符的栈op_stack，申请一个存储输出的栈output，存储规则是遇到数字直接存到output中, 运算符的处理逻辑是如果op_stack是空的，
    直接存，如果op_stack这个栈
    """
    precedence = {"!":3, "&":2, "|":1, "(":0}

    output = []
    op_stack = []

    for ch in s:
        if ch in ('0', '1'):
            output.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack and op_stack[-1] != '(':
                output.append(op_stack.pop())
            # 弹出左括号
            op_stack.pop()
        else:
            while op_stack and precedence[op_stack[-1]] >= precedence[ch]:
                output.append(op_stack.pop())
            op_stack.append(ch)

    for ch in op_stack:
        output.append(ch)

    return ''.join(output)


def calculate(s:str):

    st = []

    for ch in s:
        if ch in ('0', '1'):
            st.append(int(ch))
        elif ch == '!':
            st.append(1 - st.pop())
        elif ch == '&':
            right = st.pop()
            left = st.pop()
            st.append(left & right)
        elif ch == '|':
            right = st.pop()
            left = st.pop()
            st.append(left | right)

    return st[0]

if __name__ == "__main__":

    data = sys.stdin.read().strip()
    tokens = tokenize(data)
    print(f"tokens:{tokens}")
    post = midfixtopost(tokens)
    print(f"post:{post}")
    res = calculate(post)
    print(res)