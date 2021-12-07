horz = 0
depth = 0
aim = 0

with open('input.txt') as f:
    line = f.readline()

    while(line != ''):
        command = line.split(' ')
        print(command)

        if command[0] == 'forward':
            horz += int(command[1].strip())
            depth += aim*int(command[1].strip())
        if command[0] == 'down':
            aim += int(command[1].strip())
        if command[0] == 'up':
            aim -= int(command[1].strip())

        line = f.readline()
        
print(f'Horizontal: {horz}')
print(f'Vertical: {depth}')
print(f'Solution: {depth*horz}')

