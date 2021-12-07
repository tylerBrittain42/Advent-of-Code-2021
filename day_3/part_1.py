# 1 increments
# 0 decrements

def common_bit(code, pos, nos):
    new_code = ''
    for char in code:
        if int(char) > 0:
            new_code += pos
        else:
            new_code += nos
    return new_code




with open('input.txt') as f:
    line = f.readline()

    tracker = [0] * len(line.strip())

    while(line != ''):
        
        for i,char in enumerate(line.strip()):
            if char == '1':
                tracker[i] += 1
            else:
                tracker[i] -= 1

        line = f.readline()

    most_common = int(common_bit(tracker,'1','0'),2)
    least_common = int(common_bit(tracker,'0','1'),2)
    
    print(f'Most common: {most_common}')
    print(f'Least common: {least_common}')
    print(f'Product: {most_common * least_common}')


