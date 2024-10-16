print("Hello, welcome to grocery management program")
print('------------------------------------------------')

choice = 0
myList: list= []
count=1
addeditem= ''

while choice != 5:
    m=True
    print('Choose an option:')
    print('[1] Add an item')
    print('[2] View the list')
    print('[3] Remove an item')
    print('[4] Reset')
    print('[5] Exit')
    choice= input('Enter your choice: ')
    if choice.isdigit():
        choice= int(choice)

    match choice:
        case 1: 
            addeditem= input('Enter an item: ')
            if addeditem.isdigit():
                print('Not valid')
            else:
                myList.append(addeditem)
                print(f'Item {addeditem} has been added to your list')
        case 2:
            print('Your list:')
            for everything in myList:
                    print(f'{count}.{everything}')
                    count+=1
        case 3:
            remuv= input('What item do you want to remove: ')
            if remuv in myList:
                myList.remove(remuv)
                print(f'Item {remuv} has been removed')
            else:
                print('ITS NOT ON THE LIST')
        case 4:
            myList.clear()
            print('Your list has been reseted')
        case 5:
            break
        case _:
            print('Not valid')
    count=1
print('Bye!')