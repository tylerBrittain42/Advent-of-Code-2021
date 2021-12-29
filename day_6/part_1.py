def next_day(state):

    temp = state[0]

    for i in range(0, 8):
        state[i] = state[i+1]
    state[-1] = temp
    state[6] += temp
        
    return state

def main():

    days = 256
    state_machine = [0] * 9

    with open('input.txt') as f:
        seed = f.read().rstrip('\n').split(',')
    
    for i in seed:
        state_machine[int(i)] += 1

    for day in range(0,days):
        next_day(state_machine)
        print(f'After {day + 1} days: {state_machine} fish: {sum(state_machine)}')
    print(f'Total Fish Count: {sum(state_machine)}')

if __name__ == '__main__':
    main()