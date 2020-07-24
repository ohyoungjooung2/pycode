#
# This print hourglasses pattern below 2d array
#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 2 4 4 0
#0 0 0 2 0 0
#0 0 1 2 4 0

# To be
# 1 1 1  1 1 0  1 0 0  0 0 0
#   1      0      0      0
# 1 1 1  1 1 0  1 0 0  0 0 0

# 0 1 0  1 0 0  0 0 0  0 0 0
#   1      1      0      0
# 0 0 2  0 2 4  2 4 4  4 4 0
#Same patters goes on

#Return eash hour-glass pattern's max sum

#print(arr)
def hour_gls_max(arr):
  res=[]
  for i in range(len(arr)):
      #print(arr[i])
      for j in range(len(arr[i])):
          #print(arr[i][j:j+3],end=' ')
          #print(arr[i+1][j:j+3],end=' ')
          #print(arr[i+2][j:j+3],end=' ')
          res.append(arr[i][j:j+3]) 
          res.append(arr[i+1][j:j+3]) 
          res.append(arr[i+2][j:j+3]) 
  
          if j == 3:
             #print()
             break
       
      if i == 3:
         break
  #print(res)
  for k in range(1,len(res),3):
      res[k].pop()
      res[k].pop(0)
      #print(k)
  
  #print(res)
  
  #Start j=0
  j = 0
  
  #Max value from -36
  #
  max_val=-36
  for i in range(len(res)):
      #For debug
      #if i % 3 == 0:
      #    print("\n")
      #For debug
      #print(res[j]+res[j+1]+res[j+2])
      #print("Sum of each 3 array is ",sum(res[j]+res[j+1]+res[j+2]))
  
      if sum(res[j]+res[j+1]+res[j+2]) > max_val:
          max_val = sum(res[j]+res[j+1]+res[j+2])
      #J increase by 3
      j+=3
      #print(j)
      if i  == (len(res)-3):
         break;
      if j == (len(res)):
         break;
  return max_val 



arr = [[9,5,5,5,5,5],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
print(hour_gls_max(arr))
