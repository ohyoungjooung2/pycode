#Reverse triangle
#* * * * *
#-* * * *
#--* * *
#---* *
#----*
def revtri(n):
    for i in range(n):
        #print(i)
        for j in range(n,i,-1):
          if j == n:
            s=" "*i
            print(s,"*",end=' ')
          else:
            print("*",end=' ')

        print()

revtri(8)
