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

def filter_by_bit(bit, index, llist):
    new_list = []
    for seq in llist:
        if seq[index] == bit:
            new_list.append(seq)
    return new_list

def bit_criteria(sequence,greatest):
    print(sequence)
    for bit_index in range(len(sequence[0])):
        sig_count = 0
        for seq in sequence:
            if seq[bit_index] == '1':
                sig_count += 1
            else:
                sig_count -= 1
        print(f'sig count: {sig_count}')

        if greatest:
            if sig_count >= 0:
                sequence = filter_by_bit('1',bit_index,sequence)
            else:
                sequence = filter_by_bit('0',bit_index,sequence)
        else:
            if sig_count >= 0:
                print('FUCK')
                sequence = filter_by_bit('0',bit_index,sequence)
            else:
                sequence = filter_by_bit('1',bit_index,sequence)
        if len(sequence) == 1:
            return sequence[0]
    return sequence[0]


sequences = []

with open('input.txt') as f:
    line = f.readline()

    while(line != ''):
        sequences.append(line.strip())
        line = f.readline()
    oxygen = int(bit_criteria(sequences,True),2)
    co2 = int(bit_criteria(sequences,False),2)
    
print(f'Oxygen: {oxygen}')
print(f'CO2: {co2}')
print(f'Product: {oxygen * co2}')

