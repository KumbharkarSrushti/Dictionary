dict={"a":300,"b":200,"c":400,"e":500}
a=[]
for min in dict.values():
    a.append(min)
    i=0
    b=a[0]
    c=a[0]
    while i<len(a):
        if a[i]<b:
            b=a[i]
        i=i+1
print("minimum number:",b)


# dict={"a":400,"b":600,"c":100,"e":500,"f":800}
# a=[]
# for max in dict.values():
#     a.append(max)
#     i=0
#     b=a[0]
#     c=a[0]
#     while i<len(a):
#         if a[i]<b:
#             if a[i]>c:
#                 c=a[i]
#             b=a[i]
#         i=i+1
# print("maxmum number:",b)
# print("maximun num", c)
# print(dict)



