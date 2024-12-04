import re

data = open("day3.txt").read()


# Part 1
print(sum(int(t[0]) * int(t[1]) for t in re.compile(r'mul\((\d+),(\d+)\)').findall(data)))

# Part 2
pattern = re.compile(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))')
sum = 0
enabled = True
for match in pattern.findall(data):
    if enabled and match[0].startswith("mul"):
        sum += int(match[1]) * int(match[2])
    elif match[0].startswith("don't"):
        enabled = False
    elif match[0].startswith("do"):
        enabled = True
print(sum)
