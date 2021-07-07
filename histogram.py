a = [1,2,4,6,2,3,2,1,None,'a']


def count_elements(seq):
    hist = {}
    for x in seq:
        hist[x] = hist.get(x, 0) + 1 
    return hist

print(count_elements(a))
