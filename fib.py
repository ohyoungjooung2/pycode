#Simple fibonacci
def fib(n):
  fir=0
  secd=1
  rs=[]
  s=""
  print(fir,'',end=' ') #0
  print(secd,'',end=' ') #0
  #print(secd) #1
  rs.append(fir)
  s+=str(fir)
  s+=" "
  rs.append(secd)
  s+=str(secd)
  s+=" "
  for i in range(n):
      temp=fir #temp=0,1,1,2
      fir=secd #fir=1,1,2,3
      secd=temp+fir #secd=1,2,3,5
      print(secd,'',end=' ') #print(1,2,3,5))-(0,1,1,2,3,5)
      rs.append(secd)
      s+=str(secd)
      s+=" "

  print(secd,end=' ')
  print('')
  print(rs)
  #print(s)

fib(10)
