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
          if j == 5:
            s=" "*i
            print(s,"*",end=' ')
          else:
            print("*",end=' ')

        print()

revtri(5)
