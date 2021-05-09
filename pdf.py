#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
def pdf(a,s):
    import string
    num = [ j for j in range(0,26) ]
    ass = string.ascii_lowercase
    zip_dict = dict(zip(ass,num))
    #print(zip_dict)
    rs = []
    for sele in s:
        #print(zip_dict[sele])
        rs.append(a[zip_dict[sele]])
    #print(rs)
    rs_max = max(rs)
    return rs_max * len(s) * 1

a=[1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
print(pdf(a,s='zaba'))
