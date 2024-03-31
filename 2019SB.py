#Write a program that gets two words from the user and then displays a message
#saying if the first word can be created using the letters from the second word or not.

word = list(input())
refword = list(input())

#reflist = refword.split('')
#second = list(word)
#print(second)

truecount = 0

for i in word:
    if i in refword:
        truecount += 1
        refword.remove(i)

#for letter1 in refword:
#    #print(letter1)
#    for letter2 in word:
#        if letter1 == letter2:
#            truecount+=1
#            refword.replace(letter1, '', 1)
        
print(truecount)
if truecount == len(word):
    print("Can be made")
else:
    print("Cannot be made")