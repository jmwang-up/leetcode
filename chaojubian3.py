import sys


def midfix_to_postfix(tokens):

    precedence = {"!":3, "&":2, "|":1, "(":0}
    output = []
    op_stack = []

    for tok in tokens:
        if tok in ("0", "1"):
            output.append(tok)
        elif tok == "(":
            op_stack.append(tok)
        elif tok == ")":
            while op_stack and op_stack[-1] != '(':
                output.append(op_stack.pop())
            op_stack.pop()
        else:
            while op_stack and precedence[op_stack[-1]] >= precedence[tok]:
                output.append(op_stack.pop())
            op_stack.append(tok)
    while op_stack:
        output.append(op_stack.pop())
    return output

def cal_new_expr(expr):

    st = []
    for t in post:
        if t in ('0', '1'):
            st.append(int(t))
        elif t == '!':
            a = st.pop()
            st.append(1-a)
        elif t == '&':
            b = st.pop()
            a = st.pop()
            st.append(a & b)
        elif t == '|':
            b = st.pop()
            a = st.pop()
            st.append(a | b)
    return st[0] 

def tokenize(s:str):

    tokens = []
    i = 0
    n = len(s)

    while i < n:

        c = s[i]

        if c in '!&|()01':
            tokens.append(c)
            i += 1
        else:
            i += 1
    
    return tokens





if __name__ == "__main__":

    data = sys.stdin.read().strip()
    tokens = tokenize(data)
    print(tokens)
    post = midfix_to_postfix(tokens)
    print(post)
    res = cal_new_expr(post)
    print(res)