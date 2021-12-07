
prev_n = None
cur_n = None
desc_count = 0

cur = []
prev = []

with open('input.txt') as f:
    line = f.readline()

    while(line != ''):


        cur_n = int(line)
        cur.append(cur_n)
        if len(cur) > 3:
            cur.pop(0)
        
        if len(prev) == 3 and sum(prev) < sum(cur) and len(cur) == 3:
            desc_count += 1
            
        prev_n = int(cur_n)
        prev.append(prev_n)
        if len(prev) > 3:
            prev.pop(0)

        line = f.readline().strip()


    print(f'Solution: {desc_count}')

