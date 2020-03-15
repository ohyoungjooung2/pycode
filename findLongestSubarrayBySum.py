a=[1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,1]
#a=a*1000;
s=15
def findLongestSubarrayBySum(a):
    start=0;
    maxv=0;
    c_sum=0;
    for ar in range(start,len(a)):
     c_sum=a[ar];
     for arv in range(ar+1,len(a)): 
        c_sum+=a[arv];
        if c_sum == s:
            r=[];
            #print('hi');
            r.append(ar);
            r.append(arv);
            r2=r[1]-r[0];
            maxv=max(maxv,r2);
    return maxv;
    #return maxv;

print(findLongestSubarrayBySum(a))
