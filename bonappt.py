bill=[3,10,2,9]
k=1
b=12
def ba(bill,k,b):
    del bill[k]
    billsum=sum(bill)/2
    if b == billsum:
        return "Bon Appetit"
    else:
        return int(b-billsum)


bill=[3,10,2,9]
k=1
b=7
print(ba(bill,k,b))
