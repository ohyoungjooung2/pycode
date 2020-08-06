#
#text[0] "code", if rest is samewith code anagram "cdeo" than remove it.
#if text[1] "aaagmnrs" is samw with "aaagmnrs" then remove it,,in this case
#it is anagrams.. and so on and on..
#The result should be sorted(text) like ["aaagmnrs","code","dddd"]
text=["code","aaagmnrs","anagrams","doce","dddd"] 
res=[]
def funWithAnagrams(text):
    t2=list(text)
    for i in range(len(text)):
        for j in range(i+1,len(text)):
            #print(sorted(text[i]))
            if ''.join(sorted(text[i])) == ''.join(sorted(text[j])):
                res.append((text[j]))
                

    for r in res:
        text.remove(r)
    print(sorted(text))

    
funWithAnagrams(text)
