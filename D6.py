f = open("D6input", "r")
lines = []
for line in f:
    lines.append(line)

for element in lines:
    element = element[:-2]

print(lines)
