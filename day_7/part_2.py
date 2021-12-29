import math

def toInt(s_list):
    i_list = []
    for ele in s_list:
        i_list.append(int(ele))
    return i_list

def get_cost(final,init):
    diff = abs(final - init)
    cost = 0
    step = 0
    for i in range(0,diff):
        cost += step
        step += 1
    return cost

def generate_ref_map(upper_bound):
    last = 0
    step = 0
    ref_map = {}

    for i in range(0,upper_bound+1):
        ref_map[i] = last + step
        last = ref_map[i]
        step += 1 
    return ref_map


def main():

    mapp = {}
    ref_map = {}


    with open('input.txt') as f:
        pos = f.read().rstrip('\n').split(',')
        pos = toInt(pos)
    upper = max(pos)

    ref_map = generate_ref_map(upper)    

    for crab in pos:
        for distance in range(0,upper + 1):
            cost = ref_map[abs(crab-distance)]
            if distance in mapp:
                mapp[distance] += cost
            else:
                mapp[distance] = cost

    print(f'Solution: {min(mapp.items(), key=lambda x: x[1])}') 

if __name__ == '__main__':
    main()