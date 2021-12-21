a = []
a.append([1,1,1])


with open('input.txt') as f:
    ans = f.readline().split(',')
    print(ans)

    foo = f.readline()
    print(f'a{foo}a')
    print(foo == '\n')
    
    while (foo != ''):
        foo = f.readline()
        print(f'a{foo}a')
        if (foo == '\n'):
            print('NEW LINE HERE')
    
    
print(a)


