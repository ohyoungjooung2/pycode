#The formula is ((i//5) * 5) + 5. Multile 5 - grade value.
#If grade is less than 38, then,grades is as it is.
#If the formula - grades is more or same with 3, then  grade as it is.
#If the formula - grades is less than  3, then  grade is rounded to formula result.

def getRound(grades):
    res=[]
    for i in grades:
        compVal = ((i//5) * 5) + 5
        if compVal - i < 3 and i >= 38:
            res.append(compVal)
        if (compVal - i >= 3) or (i < 38):
            res.append(i)
    return res

grades=[80, 96, 18, 75, 80, 60, 60, 15, 45, 15, 10, 5, 46, 87, 33, 60, 14, 71, 65, 2, 5, 97, 0]
#File open to insert text's each line values to grades
#ti =  open('./t.txt','r')
#for i in ti:
    #print(i)
#    grades.append(int(i.replace('\n','')))
#ti.close
#print(grades)
    

print(getRound(grades))


   
