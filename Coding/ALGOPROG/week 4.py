# xlist= [2,1,4]
# ylist= xlist.sort()
# print(xlist,ylist)
# # print (xlist[1]+ xlist[2])
# for everyitem in [2,1,0]:
#     print (xlist[everyitem], end=" ")
# # a=1
# # b=2
# # xlist=[a,b,a+b]
# # a=0
# # b=0
# # print(xlist)

# score= ['s','c','o','r','e']
# sum=""
# for i in range(len(score)):
#     sum= score[i]+ sum
# print (sum)
# n = ''
# for i in range (5):
#     for j in range (1,i+2):
#         print(j, end="")
#     print()
# for i in range(5):
#     print("*" * (i+1))

#Pascal-triangle
# for i in range(1, 6):
#     print(" " * (5-i), end=" ")
#     for j in range(1, i+1):
#          print(j, sep="", end="")
#     for k in range(i-1, 0, -1):
#        print(k, sep="", end="")
#     print()
# xlist = [1, [1, 2], [1, 2, 3]]
# print(xlist[1][1])
# xlist = [1, [1, 2], [1, 2, 3]]
# print(xlist[1] + [3])

# def sum_part(a, n):
#     sum = 0
#     for x in a[n]:
#             sum = sum + x
#     return sum
# ylist = [[1, 2], [3, 4], [5, 6], [7, 8]]
# x = sum_part(ylist, 2)
# print(x)

# xlist= [[1,2]]
# sum = 0
# for i in range(len(xlist)):
#     sum = sum + xlist[i][1]
# print(sum)
# for i in range(3):
#     for j in range(3):
#         print(i * j, end="")
# s = "abc"
# for i in range(1, len(s) + 1):
#     sub = ""
#     for j in range(i):
#         sub = s[j] + sub
#     print(sub)
# x = [7]
# y = x
# x[0] = x[0] + 3
# y[0] = y[0] - 5
# print(x, y)
# x = [7]
# y = x
# x = [8]
# print(x, y)
x = [1, 2, 3, 4]
y = x
y[2] = 0
z = x[1 : ]
x[1] = 9
print(x, y, z)