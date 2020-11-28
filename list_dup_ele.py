#Simple py code to find list element's index number
#Ex) if you want to find 2's index number in list then, should print
#[3,6]
list1=["oyj","oyj",1,2,3,4,2]
def listdu(tg_list,n):
    tgl=[]
    for i in range(len(tg_list)):
        if tg_list[i] == n:
           tgl.append(i)
    print(tgl)


listdu(list1,"oyj")
listdu(list1,1)
listdu(list1,2)

