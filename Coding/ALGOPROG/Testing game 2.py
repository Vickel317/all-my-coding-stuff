import random 

city_zones = {
    'Zone A': ['power cell', 'hazard', 'battery pack'],
    'Zone B': ['power cell', 'battery pack', 'hazard'],
    'Zone C': ['zonk','hazard', 'power cell','power cell'],
    'Zone D': ['power cell','hazard','battery pack','dust'],
    'Zone E': ['power cell', 'power cell', 'hazard'],
}
inventory = []
battery_level = 8
max_bat = 10
collected_cells = 0
total_cells= sum(zonevalue.count('power cell') for zonevalue in city_zones.values())

while battery_level != 0:
    user_input= input ("Where d'ya wanna go? (Zone A, Zone B, Zone C, Zone D) or d'ya want to check ya' inventory? ('inventory') ")
    match user_input:
        case "Zone A": 
            battery_level -=1
            randitem= random.choices(city_zones.values['Zone A'])
            if randitem == 'powercell':
                inventory.append(item)
                collected_cells +=1
                print(f'Congrats! you found powercell\n adding it to the stack: {collected_cells}/{total_cells}')
            elif randitem == 'hazard':
                battery_level -= 1
                print(f"Collected: {item}. Your battery is drained by one: {battery_level}/{max_bat}.")
            elif item == 'battery_pack':
                battery_level += 3
                print(f"Collected: {item}. You gained one battery: {battery_level}/{max_bat}.")
            else:
                print(f"Ha. Better luck next time.")
        case "Zone B":
            print('Your list:')
            for everything in myList:
                    print(f'{count}.{everything}')
                    count+=1
        case 'Zone C':
            remuv= input('What item do you want to remove: ')
            if remuv in myList:
                myList.remove(remuv)
                print(f'Item {remuv} has been removed')
            else:
                print('ITS NOT ON THE LIST')
        case "Zone D":
            myList.clear()
            print('Your list has been reseted')
        case 5:
            break
        case _:
            print('Not valid')