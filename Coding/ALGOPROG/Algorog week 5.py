# atta= 'gay'
# print (f'Atta is {atta}'

# def atta(x,y):
#     while x < 10:
#         print (y)

# atta(5, 10)

#void- won't return anythin/ non-void - return<<var>
'''
def funcName (<parameter>)
parameter is sumth that the function need to have so it could run

return is used to store a value inside a placeholder

to call a fuction we need to give a placeholder 

myList= [] = mutable, sequential -index
mySet= {} = mutable, unordered, unique
myTuple= () = imutable, sequential - index
myStr= "," = imutable, sequential -index
myDict = {<keys>:<value>} - mutable, unordered
get function= if it exist it calls the value, if it doesn't exist it'll show none or call the second value you assign with it
'''

# def demoDefault(a,b=3):
#     print (a+b)

# y=10
# demoDefault(y)

# def f(x):
#     return x + 2, x * 2
# x, y = f(5)
# print(x + y)

# def calc_q1(x):
#     q = 4 * x + 1
#     return q
# q= calc_q1(5)
# print(q)
# def calc_q2(x):
#     q = 4 * x + 1
#     print(q)
# q = calc_q2(5)
# q = 20
# def calc_q3(x):
#     q = 4 * x + 1
#     return q
# q = calc_q3(5)
# def calc_q4(x):
#     q = 4 * x + 1
# print(calc_q4(5))
# abc = 5 + 6 // 12
# print(abc)
# def = 5 + 6 % 7
# print(def)
# def get_input():
#     x = float(input("Enter a number: "))
#     return x
# def main():
#     get_input()
#     print(x ** 2)
# main()
# def get_input():
#     x = float(input("Enter a number: "))
#     return x
# def main():
#     print(get_input() ** 2)
# main()
# def f3(x, y = 2):
#     return (x + 1) / (y - 1)
# z = f3(3, 3) + 1
# print (z)

# def f1(x, y):
#     print((x + 1) / (y - 1))
# z = f1(3, 3) + 1

# def f2(x, y):
#     return (x + 1) / (y - 1)
# z = f2(3, 3) + 1
# print (z)

# def f3(x, y = 2):
#     return (x + 1) / (y - 1)
# z = f3(3) + 1

# print(z)

# def inc_by_two(x):
#     x = x + 2
#     return x
# x = 10
# x= inc_by_two(x)
# print("x = ", x)

# Rafie= {'name': 'Rafie', 'Age' : 17 ,'height' : 160}

# for item in Rafie:
#     print(item)

# for item in Rafie.keys():
#     print (item)

# for item in Rafie.values():
#     print (item)

# for key in Rafie:
#     print(f'{key} : {Rafie[key]}') #Rafie [key] give back the value

# for key, value in Rafie.items():
#     print (f'{key} : {value}')

# d = {'a' : 0, 'b': 1, 'c' : 2}
# print(d[2])

d = {'a' : 0, 'b': 1, 'c' : 2}
# print(d.get(c))
# for x in sorted(d):
#     print(sorted(d))
#     print(x)
#     print(d[x], end=" ")
# for x in sorted(d.items()):
#     print(x, end=" ")   
# for x in sorted(d.keys()):
#     print(x, end=" ")
pres = {'george' : 'washington', 'thomas' : 'jefferson','john' : 'adams'}
# print(pres.get('washington', 'dc'))
for p in sorted(pres):
    print(p, end=" ")