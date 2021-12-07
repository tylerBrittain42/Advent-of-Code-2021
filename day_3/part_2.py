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

def bit_criteria(sequence):


sequences = []
ones = 0

with open('input.txt') as f:
    line = f.readline()

    while(line != ''):
        sequences.append(line.strip())
        line = f.readline()
    
    for bit_index in range(len(sequences[0])):
        for seq in sequences:
            if seq[bit_index] == '1':
                ones += 1
        if ones >= len(sequences)/2:
            print('1')
            sequences = filter_by_bit('1',bit_index,sequences)
        else:
            print('0')
            sequences = filter_by_bit('0',bit_index,sequences)
        ones = 0
print(sequences)

# print(sequences)

