def toInt(s_list):
    i_list = []
    for ele in s_list:
        i_list.append(int(ele))
    return i_list


def main():

    mapp = {}

    with open('input.txt') as f:
        pos = f.read().rstrip('\n').split(',')
        pos = toInt(pos)
    upper = max(pos)


    for crab in pos:
        for distance in range(0,upper + 1):
            cost = abs(crab - distance)
            if distance in mapp:
                mapp[distance] += cost
            else:
                mapp[distance] = cost
    print(min(mapp.items(), key=lambda x: x[1])) 

if __name__ == '__main__':
    main()