d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# d3=dict()
# d3.update(d1)
# d3.update(d2)
# print(d3)
for i in d2 :
    if i in d1 :
        d1[ i ] = d1[ i ] +d2[ i ]
    else :
        d1[ i ] = d2[ i ]
print(d1)