# alphabetizies a string
def alpha(sstring):
    return ''.join(sorted(sstring))

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

# Checks if all the characters in a given string are in another string
def has(big, small):
    while len(small) > 0:
        if small[0] in big:
            small = small.replace(small[0],'')
        else:
            return False
    return True

# returns a key, given a value
def val_to_key(mapp, val):
    return list(mapp.keys())[list(mapp.values()).index(val)]


def main():

    sum = 0    
    with open('input.txt') as f:

        line = f.readline()
        while(line):

            # values that we still need to find
            toFind = [0,1,2,3,4,5,6,7,8,9]

            # len of unique vals and ref map
            unique_lengths = [2,3,4,7,8]
            # Len : Val
            unique = {2:1,3:7,4:4,7:8}
            # ans key that we are building
            key = {}

            # getting input
            line = line.rstrip('\n').split('|')
            patterns = line[0].split(' ')
            outputs = line[1].split(' ')

            # making data alphabetical
            outputs = list(map(alpha,outputs))
            patterns = list(map(alpha,patterns))

            # Finding the unique values
            for i in patterns:      
                if len(i) in unique_lengths:
                    key[i] = unique[len(i)]
                    unique_lengths.remove(len(i))
                    toFind.remove(unique[len(i)]) 

                        
            # grabbing nonunique values by length
            fives = []
            sixes = []
            for i in patterns:
                if len(i) == 5:
                    fives.append(i)
                elif len(i) == 6:
                    sixes.append(i)
        
            # Finding 3 by overlaying 7
            for i in fives:
                if has(i,val_to_key(key,7)):
                    key[i] = 3
                    toFind.remove(3)
                    break
            fives.remove(val_to_key(key,3))

            # Finding 9 by overlaying 4
            for i in sixes:
                if has(i,val_to_key(key,4)):
                    key[i] = 9
                    toFind.remove(9)
                    break
            sixes.remove(val_to_key(key,9))

            # Finding zero by overlaying 7
            for i in sixes:
                if has(i,val_to_key(key,7)):
                    key[i] = 0
                    toFind.remove(0)
                    break

            # The remaining value must be 6
            sixes.remove(val_to_key(key,0))
            key[sixes[0]] = 6
            toFind.remove(6)

            if len(isMissing(val_to_key(key,4),fives[0])) == 3:
                key[fives[0]] = 5
                key[fives[1]] = 2
            else:
                key[fives[0]] = 2
                key[fives[1]] = 5
            toFind.remove(2)
            toFind.remove(5)
                            
            line = f.readline()

            
            # parse answer
            ans = []

            while '' in outputs:
                outputs.remove('')

            for i in outputs:
                ans.append(str(key[i]))
            ans = ''.join(ans)
            
            sum += int(ans)

        print(sum)

if __name__ == '__main__':
    main()