import random #import random so we can use random function

city_zones = { #what you can find in each zone
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
total_cells= sum(zonevalue.count('power cell') for zonevalue in city_zones.values()) #total cells according to dictionaries

def move_to_zone(zone): #changing zone to zone require 1 battery
    global battery_level #calling battery level from global variable
    if zone in city_zones:
        print(f'You wander into {zone}')
        battery_level -=1
        search_item(zone)
    else:
        print ("It's not in tha map!")

def search_item(item):
    global collected_cells, total_cells, battery_level, max_bat
    randitem = random.choice(list(city_zones.values())[random.randint(0, len(city_zones) - 1)]) #calling random item from city zone

    if randitem == 'power cell':
        inventory.append('power cell')
        collected_cells +=1
        print(f'Congrats! you found powercell\n adding it to the stack: {collected_cells}/{total_cells}')
    elif randitem == 'hazard':
        battery_level -= 1
        print(f"Collected: Hazard. Your battery is drained by one: {battery_level}/{max_bat}.")
    elif randitem == 'battery pack':
        battery_level += 3
        print(f"Collected: Battery Pack. You gained one battery: {battery_level}/{max_bat}.")
    else:
        print(f"Ha. Better luck next time.")

def display_inventory(): # displaying inventory
    print ("Your robot's inventory: ", inventory)

def gamestatus(): #End result
    if battery_level <= 0:
        print('BEEP BOOP BATTERY DEPLETED. GAME OVER')
        return True
    elif collected_cells == total_cells:
        print('YOU FOUND IT ALL! CONGRATS YOU WIN!')
        return True
    else:
        return False

while True: #Loop of the game
    print(f'Battery level: {battery_level}/ {max_bat}')
    user_input= input ("Where d'ya wanna go? (Zone A, Zone B, Zone C, Zone D, Zone E) or d'ya want to check ya' inventory? ('inventory') ").strip()

    if user_input.lower() == 'inventory':
        display_inventory()
    else: 
        move_to_zone(user_input)
    if gamestatus():
        break