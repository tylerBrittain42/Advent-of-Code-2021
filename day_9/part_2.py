

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


def bfs_size(map,root):

    to_visit = []
    to_visit.append(root)

    visited = []
    visited.append(root)


    while len(to_visit) > 0:
        node = to_visit.pop(0)
        # visited.append(node)

        # print(node)

        neighbors = explore(map,node[0],node[1])
        for i in neighbors:
            if i not in visited and map[i[0]][i[1]] != 9:
                visited.append(i)
                to_visit.append(i)
        



    return len(visited)


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
  
    return neighbors




def main():
    
    map = []
    low_points =[]
    biggest = []

    # set up
    with open('/home/tyler/Documents/assorted_code/Advent-of-Code-2021/day_9/input.txt') as f:
        line = f.readline().rstrip('\n')
        while line:
            map.append(toArray(line))
            line = f.readline().rstrip('\n')
    
    for i, row in enumerate(map):
        for j, ele in enumerate(row):
            if isLow(map,i,j):
                low_points.append([i,j])
    
    for i in low_points:
        biggest.append(bfs_size(map,i))
    biggest.sort(reverse=True)
    print(biggest)

    print(f' The product of {biggest[0]} x {biggest[1]} x {biggest[2]} is {biggest[0]*biggest[1]*biggest[2]}')

if __name__ == '__main__':
    main()