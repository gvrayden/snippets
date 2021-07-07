a = [1,2,[3,4, [5],[6,7,[8,[9]]]]]

def flatten(seq, l):
    for x in seq:
        if isinstance(x, list):
            l.extend(flatten(x,l))
        else:
            l.append(x)
l = []
print(list(flatten(a, l)))