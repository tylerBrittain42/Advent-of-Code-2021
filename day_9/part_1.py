def toArray(input):
    return list(map(int,list(input)))

def isLow(map, i, j):
    y_bound = len(map)
    x_bound = len(map[0])
    cur = map[i][j]

    # above check
    if i > 0:
        if cur - map[i-1][j] >= 0:
            return False
    
    # below check
    if i + 1 < y_bound:
        if cur - map[i+1][j] >= 0:
            return False

    # left check
    if j > 0:
        if cur - map[i][j-1] >= 0:
            return False

    # right
    if j + 1 < x_bound:
        if cur - map[i][j+1] >= 0:
            return False


    return True

def main():
    
    map = []
    sum = 0

    # set up
    with open('/home/tyler/Documents/assorted_code/Advent-of-Code-2021/day_9/input.txt') as f:
        line = f.readline().rstrip('\n')
        while line:
            map.append(toArray(line))
            line = f.readline().rstrip('\n')
    
    for i, row in enumerate(map):
        for j, ele in enumerate(row):
            if isLow(map,i,j):
                sum += map[i][j] + 1
    
    print(sum)

if __name__ == '__main__':
    main()