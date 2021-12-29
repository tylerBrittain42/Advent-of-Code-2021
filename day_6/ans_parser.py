# Parses example answers to script format
foo = '4,5,4,2,3,4,5,6,6,7'

foo = foo.split(',')
countt = [0] * 9

for i in range(0, len(countt)):
    countt[i] = foo.count(str(i))

print(countt)
# 3 days
#  [2, 1, 0, 0, 0, 1, 1, 1, 1]

# 1 day
#  [1, 1, 2, 1, 0, 0, 0, 0, 0]

# day 2
# [1, 2, 1, 0, 0, 0, 1, 0, 1]