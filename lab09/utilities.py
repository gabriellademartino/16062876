data = [1,23,3,45,5,64,7,8,93,3,10,11,12,13,14,15,16,17,555,33,4343,31]
e = 10


def lin_find(x,y):
    count = 0
    z = sorted(x)
    for n in range(len(x)):
        if z[n] == y:
            return n + 1
        else:
            count = count + 1
    else:
        return None

    print count

# looks through the ordered list finding the number
# returns the place if it is there, and None if it is not

#the counter to count how many times it goes through the loop isn't working though


if lin_find(data,e) == None:
    print 'The number', e, 'does not appear in the list.'
else:
    print 'The number', e, 'appears at place', lin_find(data,e), 'in the sorted list.'

def bin_find(u, v):
    count = 0
    s = sorted(u)
    a = 0
    b = len(s)
    while a < b:
        m = (a+b)//2
        i = s[m]
        if i < v:
            a = m + 1
            count = count + 1
            # if the value is bigger than the the middle place, take the upper half
        elif i > v:
            b = m
            count = count + 1
            # if the value is less take the lower half
        else:
            return m + 1
            # if the value is the same finish and return the place in the list
    print count

# counter not working on this either


if bin_find(data,e) == None:
    print 'The number', e, 'does not appear in the list.'
else:
    print 'The number', e, 'appears at place', bin_find(data,e), 'in the sorted list.'
