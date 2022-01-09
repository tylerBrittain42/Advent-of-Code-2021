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


def bfs_size(map,low_points):

    low_points = [0,0]
    queue = []
    queue.append(low_points)
    queue.extend(explore(map,low_points[0],low_points[1]))
    visited = low_points
    visited.extend([explore(map,low_points[0],low_points[1])])

    count = 0
    while len(queue) != 0:

        # adding a new node
        node = queue.pop(0)
        visited.append(node)

        # adding node's nieghbors
        neighbors = explore(map, node[0],node[1])
        for point in neighbors:
            if point not in visited:
                queue.append(point)

        print(f'{node}: {map[node[0]][node[1]]}')
        
        count += 1
        if count == 10 : 
            return
    return

#returns list of adjacent points in clockwise formation
def explore(map,row,col):

    max_row = len(map)
    max_col = len(map[0])
    neighbors = []

    # above
    if row > 0:
        neighbors.append([row - 1 , col])

    # right
    if col + 1 < max_col:
        neighbors.append([row, col + 1])

    # below
    if row + 1 < max_row:
        neighbors.append([row + 1, col])

    # left
    if col > 0:
        neighbors.append([row, col - 1])

    

    # for i in neighbors:
    #     print(f'{i}: {map[i[0]][i[1]]}')    
    return neighbors




def main():
    
    map = []
    low_points =[]
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
                low_points.append([i,j])
    
    # print(sum)
    # print(low_points)

    # bfs_size(map,low_points)
    explore(map,1,1)
if __name__ == '__main__':
    main()