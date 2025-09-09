# write the function to remove the word from list and strip ir at dsame time 
def rem(l,word):
    n =[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return  n             



l=["aahan","aayat","ali"]    
print(rem(l,"aa"))