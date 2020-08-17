#This remove from string 'dd','aa' like duplicated strings until all string's chars are not duplicated continously like 'dd','zz','cc' and so on.
#s='acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj'
def rdstr(s):
    i=0
    ll=list(s)
    while i < len(ll)-1:
        if ll[i]==ll[i+1]:
            del ll[i]
            del ll[i]
            i=0
        else:
            i+=1

    if len(ll)==0:
        return 'Empty String'
    else:

      return ''.join(ll)
           

s='abbac'
s='acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj'
print(rdstr(s))
