horz = 0
vert = 0

with open('input.txt') as f:
    line = f.readline()

    while(line != ''):
        command = line.split(' ')
        print(command)

        if command[0] == 'forward':
            horz += int(command[1].strip())
        if command[0] == 'down':
            vert += int(command[1].strip())
        if command[0] == 'up':
            vert -= int(command[1].strip())

        line = f.readline()
        
print(f'Horizontal: {horz}')
print(f'Vertical: {vert}')

