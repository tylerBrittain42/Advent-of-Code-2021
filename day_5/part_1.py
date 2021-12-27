def find_points(input):
    possible_points = []
    

    # parsing input
    split_coordinates = input.rstrip('\n').split(' -> ')
    x1 = int(split_coordinates[0].split(',')[0])
    y1 = int(split_coordinates[0].split(',')[1])
    x2 = int(split_coordinates[1].split(',')[0])
    y2 = int(split_coordinates[1].split(',')[1])

    # x == x
    if x1 == x2:
        for i in range(min(y1,y2),max(y1,y2)+1):
           possible_points.append(f'{x1},{i}')

    # y == y
    elif y1 == y2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            possible_points.append(f'{i},{y1}')


    return(possible_points)
    # print(split_co
    # ordinates)




def main():

    mapp = {}
    count = 0

    with open('input.txt') as f:
        line = f.readline()
        while(line):
            possible_points = find_points(line)

            for ele in possible_points:
                if ele not in mapp:
                    mapp[ele] = 1
                else:
                    mapp[ele] += 1

            line = f.readline()
    
    for ele in mapp.values():
        if ele > 1:
            count +=1

    # for key, value in mapp.items():
    #     if value > 1:
    #         print(key)

    print(f'The number of overlapping points is {count}')



if __name__ == '__main__':
    main()