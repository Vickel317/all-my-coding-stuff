# Create a text file and write some content to it
file_path = 'quest.txt'

with open(file_path, 'w') as file:
    name = input('Enter your name: ')
    file.write(f'Name: {name}\nWelcome to the quest!\n')