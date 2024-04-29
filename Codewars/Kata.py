def filter_list(l): # Can use try except to filter list
    output = []
    for x in l:
        try:
            x / 12
            output.append(x)
        except:
            pass
            
    return output

def reverse_words(text): # Use of map and join
    wordlist = text.split(" ")
    x = list(map(reverse, wordlist))
    return ' '.join(x)
    
def reverse(word): # How to reverse a string
    return word[::-1]

def add_binary(a,b): # Convert integer to binary
    return bin(a+b)[2:] # [2:] removes left two chars from a string

def digital_root(n):
    nlist = [int(x) for x in str(n)]
    if len(nlist) == 1:
        return nlist[0]
    else: # join only works on lists of strings
        return nlist[0] + digital_root(int(''.join(map(str, nlist[1:]))))
    # For the rest of the functionality, need to use the sum function on the list and then recursively check if the value is below 10
    
def find_nb(m):
    count = 0
    while m != 0:
        m = m - count*count*count
        count += 1
    return count - 1

print(find_nb(441))