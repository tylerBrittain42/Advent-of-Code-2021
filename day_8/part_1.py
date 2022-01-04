def main():
    
    count = 0
    ans = []
    with open('input.txt') as f:

        line = f.readline()

        while(line):
            line = line.rstrip('\n').split('|')
            patterns = line[0].split(' ')
            outputs = line[1].split(' ')


            for i in outputs:
                if len(i) in [2,3,4,7,8]:
                    count += 1
                    ans.append(i)
                
            line = f.readline()
            
    print(f'Unique digits appear {count} times')

if __name__ == '__main__':
    main()