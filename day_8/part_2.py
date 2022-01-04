class decNum:
    
    def __init__(self, val, length):
        self.real = val
        self.length = length
        self.grid = [None]*7
        # print(self.grid)

    def __repr__(self) -> str:
        return f'{self.real} {self.length}'


def alpha(sstring):
    return ''.join(sorted(sstring))

def char_count(sstring, target):
    count = 0
    for char in sstring:
        if char == target:
            count += 1
    return count

# returns a list of characters that are not shared by the two strings
def isMissing(s1, s2):
    missing = []
    if len(s1) >= len(s2):
        big = s1
        small = s2
    else:
        big = s2
        small = s1

    while len(big) > 0:
        if big[0] in small:
            small = small.replace(big[0],'')
        else:
            missing.append(big[0])
        big = big.replace(big[0],'')
    
    if len(small) > 0:
        for i in small:
            missing.append(i)

    return sorted(missing)

def has(big, small):
    while len(small) > 0:
        if small[0] in big:
            small = small.replace(small[0],'')
        else:
            return False
    return True

def val_to_key(mapp, val):
    return list(mapp.keys())[list(mapp.values()).index(val)]

def main():

    letters = ['a','b','c','d','e','f','g']
    
    # values that we still need to find
    toFind = [0,1,2,3,4,5,6,7,8,9]

    # len of unique vals and ref map
    toFind_u = [2,3,4,7,8]
    unique = {2:1,3:7,4:4,7:8}

    table = [None] * 7

    num_to_code = {}


    numToLength = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}

    # ans key that we are building
    key = {}

    with open('input.txt') as f:

        line = f.readline()

        while(line):

            # getting input
            line = line.rstrip('\n').split('|')
            patterns = line[0].split(' ')
            outputs = line[1].split(' ')

            # making data alphabetical
            outputs = map(alpha,outputs)
            patterns = map(alpha,patterns)


            # Filtering out for unique values                
            # for i in outputs:      
            #     if len(i) in toFind_u:
            #         key[i] = unique[len(i)]
            #         toFind_u.remove(len(i))
            #         toFind.remove(unique[len(i)])

            for i in patterns:      
                if len(i) in toFind_u:
                    key[i] = unique[len(i)]
                    toFind_u.remove(len(i))
                    toFind.remove(unique[len(i)])

            for char in letters:
                cur_count = char_count(line[0],char)
                if cur_count == 7:
                    table[3] = char
                elif cur_count == 4:
                    table[4] = char
                elif cur_count == 9:
                    table[5] = char

            table[0] = isMissing(val_to_key(key,1),val_to_key(key,7))[0]

            print(table)

            
                
            line = f.readline()

            # print(has('abc','as'))

            print(key)
            finding_b = isMissing(val_to_key(key,4),val_to_key(key,7))

            print(finding_b)
            

if __name__ == '__main__':
    main()