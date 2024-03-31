decimal = int(input('Enter a decimal number: '))

outputlist = []

while decimal // 2 != 0:
    outputlist.append(decimal % 2)
    decimal = decimal // 2

outputlist.append(1)

outputlist.reverse()

outputstring = ''.join(str(x) for x in outputlist)

print(outputstring)









