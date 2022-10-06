command = ''
coffee_count = 0
while command != 'END':
    command = input()
    if command.lower() == 'coding'\
        or command.lower() == 'dog'\
        or command.lower() == 'cat'\
        or command.lower() == 'movie':
        if command.islower():
            coffee_count += 1
        elif command.isupper():
            coffee_count += 2
if coffee_count > 5:
    print('You need extra sleep')
else:
    print(f'{coffee_count}')