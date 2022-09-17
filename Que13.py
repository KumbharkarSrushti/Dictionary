# a={"srushti":1,"mayu":2,"mayuri":3,"sejal":4}
# b=[]
# for key in a.keys():
#     b.append(key)
# print(b)
# c=[]
# for value in a.values():
#     c.append(value)


# a={1:20,2:40,4:60}
# b={5:50,6:60,7:70}
# c={}
# c.update(a)
# c.update(b)
# print(c)


# a={"srushti":1,"mayu":2,"mayuri":3,"sejal":4}
# b=[]
# for key in a.keys():
#     b.append(key)
# print(b)
# c=[]
# for value in a.values():
#     c.append(value)
# print(c)


# a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# a.sort()
# print(a)


# b=[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# b.sort()
# print(b)


# list1=[10,13,12,15,16,17,30,28,29]
# list2=[10,23,10,13,15,30,45,28,17]
# b=[]
# i=0
# while i<len(list1):
#     if list1[i]==list2[i]:
#         b.append(list1[i])
#     i=i+1
# print(b)



# a=[3,34,16,18,15,50,4,10]
# print(a[6])


# n=5
# i=1
# a=65
# while i<=n:
#     j=1
#     while j<=5:
#         print(chr(a),end=" ")
#         j=j+1
#         a=a+1
#     i=i+1
#     print()


a=[5,7,9,8,10,11,12,95]
input=int(input("enter the number"))
i=0
count=0
while i < len(a):
    if input<a[i]:
        count=count+1
    i=i+1
print(count)

