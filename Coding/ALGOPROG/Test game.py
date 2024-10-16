# Game setup
city_zones = {
    'Zone A': ['power cell', 'hazard', 'battery pack'],
    'Zone B': ['power cell', 'battery pack', 'hazard'],
    'Zone C': ['zonk','hazard', 'power cell','power cell'],
    'Zone D': ['power cell','hazard','battery pack','dust'],
}

robot_inventory = []
battery_level = 3  # Start with 5 battery units
max_battery = 10
collected_cells = 0
total_cells = sum(zonevalue.count('power cell') for zonevalue in city_zones.values())

def move_to_zone(zone):
    global battery_level
    if zone in city_zones:
        print(f"Moving to {zone}...")
        battery_level -= 1
        search_zone(zone)
    else:
        print("Invalid zone!")

def search_zone(zone):
    global collected_cells
    items = city_zones[zone]
    print(f"You found items in {zone}: {', '.join(items)}")
    for item in items:
        if item == 'power cell':
            collect_item(item)
def collect_item(item):
    global collected_cells
    if item == 'power cell':
        robot_inventory.append(item)
        collected_cells += 1
        print(f"Collected: {item}. Total power cells: {collected_cells}/{total_cells}.")
    elif item == 'hazard':
        battery_level -=1
        print(f"Collected: {item}. Your battery is drained by one: {battery_level}/{max_battery}.")
    elif item == 'battery_pack':
        battery_level += 3
        print(f"Collected: {item}. You gained one battery: {battery_level}/{max_battery}.")
    else:
        print(f"Ha. Better luck next time.")

def display_inventory():
    print("Current inventory:", robot_inventory)

def check_game_status():
    if battery_level <= 0:
        print("Battery depleted! Game over.")
        return True
    elif collected_cells == total_cells:
        print("All power cells collected! You win!")
        return True
    else:
      return False

# Game loop
while True:
    print(f"\nBattery Level: {battery_level}/{max_battery}")
    user_input = input("Enter a zone to move to (Zone A, Zone B, Zone C, Zone D) or 'inventory' to check your inventory: ").strip()
    
    if user_input.lower() == 'inventory':
        display_inventory()
    else:
        move_to_zone(user_input)
    
    if check_game_status():
        break