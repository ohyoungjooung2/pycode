#x^2 + y^2 = r^2 equation
def circle_draw(n):
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if(i*i + j*j <= n*n):
              print("*",end='')
            else:
              print(" ",end='')
        print("")

circle_draw(30)
