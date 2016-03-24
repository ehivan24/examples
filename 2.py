from time import time

start = time()
for i in range(1,200):
    i += 1
#print i

end = time()

elapsed = start - end

print elapsed


def find_max(data):

    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest =  val
    return biggest


data = [23,3,1,4,35,12]
print find_max(data)





def disjoint(A,B,C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

A = [1,2,3,7 ,5]
B = [34,46,7,30,23]
C = [78, 90, 45, 7, 67]



print disjoint(A, B, C)