
prev = None
desc_count = 0

with open('input.txt') as f:
    line = f.readline()

    while(line != ''):
        
        current = int(line)

        if prev != None and prev < current:
            desc_count += 1

        prev = current
        line = f.readline().strip()


    print(f'Solution: {desc_count}')