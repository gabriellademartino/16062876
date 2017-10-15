mylist1 = [1,2,3,4,5,6,7,8,9,10]
mylist2 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

len(mylist1)
len(mylist2)

mylist1 + mylist2

mylist2[3]

"Friday" in mylist2
"0" in mylist1

mylist1[3:5]
mylist2[2:len(mylist2)]

mylist1.index(7)
mylist2.index("Tuesday")

mylist = [123, 456, 789, 'abc', 'def', 'ghi']

mylist[5] = 'xyz'

mylist.append('pqr')

mylist.remove(456)

mylist.extend(mylist1)

mylist.reverse()

mylist.sort()


try:
    mylist1.remove(999)
except:
    print 'Hello'

try:
    mylist2.index("January")
except:
    print 'that aint a weekday'