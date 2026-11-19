import re

s = input()
p = input()

pattern = ''.join(
    '[a-z0-9]*' if c == '*'
    else '[a-z0-9]' if c == '?'
    else re.escape(c)
    for c in s
)

matched = re.fullmatch(pattern, p, flags=re.I | re.ASCII)
print('true' if matched else 'false')