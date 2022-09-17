# Sample_Data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# d1 = [z for z in Sample_Data for z in z.items()]
# print(dict(d1))



# s= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# a = set()
# for i in s:
#     for j in i.values():
#         a.add(j)
# print(a)


# # accending order question
# l=[1,4,5,3,9,10,23,45,64,93]
# i=0
# while i<len(l):
#     b=0
#     while b<len(l):
#         if l[i]<=l[b]:
#             c=l[i]
#             l[i]=l[b]
#             l[b]=c
#         b=b+1
#     i=i+1
# print(l)