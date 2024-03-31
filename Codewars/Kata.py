def filter_list(l): # Can use try except to filter list
    output = []
    for x in l:
        try:
            x / 12
            output.append(x)
        except:
            pass
            
    return output

def 