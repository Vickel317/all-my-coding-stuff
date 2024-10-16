# # # print('BINGO')
# # # inp= int(input("Enter a number between 1-75: "))
# # # if 0< inp <=15:
# # #     print("Belong to B")
# # # elif 16<= inp <=30:
# # #     print("Belong to I")
# # # elif 31 <= inp <= 45:
# # #     print("Belong to N")
# # # elif 46 <= inp <=60:
# # #     print ("Belong to G")
# # # elif 61<= inp <= 75:
# # #     print("Belongs to O")
# # # else:
# # #     print("Wrong number")


# # x=0
# # y=0
# # choice= 0
# # while choice!= 4:
# #     print('[1]Location')
# #     print('[2] Move')
# #     print('[3] Reset')
# #     print('[4]Quit')
# #     choice= int(input('choice: '))

# #     match choice:
# #         case 1: print(f"Robby is in ({x},{y})")
# #         case 2: 
# #             direction= input("Direction (N,E,W,S): ")
# #             distance= int(input("Distance: "))
# #             if direction== 'N':
# #                 y+=distance
# #                 print(f'Robby moved to North with a distance of ({x},{y})')
# #             elif direction== 'E':
# #                 x+=distance
# #                 print(f'Robby moved to East with a distance of ({x},{y})')
# #             elif direction== 'W':
# #                 x-=distance
# #                 print(f'Robby moved to West with a distance of ({x},{y})')
# #             elif direction== 'S':
# #                 y-=distance
# #                 print(f'Robby moved to South with a distance of ({x},{y})')
        
# #         case 3: 
# #             x=y=0
# #             print(f"Robby reset at {x},{y} [Original]")
# #         case 4: break
# #         case _: print("not valid")
# # print('Bye!')

myList: list= ['lmao', 2, 4/2, True]
secondlist: list= [1,56,3,6,3,2,1]
thirdlist: list= [1,2,4,34,234,2,[1,2,3]]
print(myList, type(myList), len(myList))

myList.append("ANYYYTHING")

print(myList, len(myList))

secondlist.sort(reverse=True)
print(secondlist)

print(thirdlist[-1][0])

count=1
for everything in myList:
    print(f'{count}.{everything}')
    count +=1

print (len(myList))