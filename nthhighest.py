a = {'a':1,'b':1, 'c':10,'d':11,'e':4}
t = [(x[1],x[0]) for x in a.items()]
import heapq
nlargest = heapq.nsmallest(1, set([x[0] for x in t]))[-1]
p = sorted([x for x in t if x[0] == nlargest], key = lambda x: x[1])
print(p)