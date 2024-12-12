import re

pattern = r"mul\((\d{1,3},\d{1,3})\)|(don't\(\))|(do\(\))"

with open('test.txt', "r") as f:
    file = f.read()


p = re.compile(pattern)
matches = p.findall(file)
answer = 0

exclude = False
for match in matches:
    mul_input, not_include, include = match
    if not_include:
        exclude = True
    elif include:
        exclude = False
    elif exclude == False:
        x, y = mul_input.split(',')
        mul_result = int(x) * int(y)
        answer += mul_result


print(answer)
