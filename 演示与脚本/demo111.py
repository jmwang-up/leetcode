s = "12+3-11"
operators = set("+-*/")
result = ""

for ch in s:
    if ch in operators:
        result += " " + ch + " "
    else:
        result += ch

print(result)  # 12 + 3 - 11