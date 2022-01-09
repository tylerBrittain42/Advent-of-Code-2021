
class Stack:
    def __init__(self):
        self.stack = []
    def add(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]


def is_valid(sequence, openn, close):

    stack = Stack()

    for char in sequence:
        if char in openn:
            stack.add(char)
        elif char in close:
            match = openn[close.index(char)]
            if stack.pop() != match:
                return False 
    return True

def calc_score(sequence, openn, close):
    
    points = {')':3 ,']':57 ,'}':1197 ,'>':25137}

    stack = Stack()


    for char in sequence:
        if char in openn:
            stack.add(char)
        elif char in close:
            match = openn[close.index(char)]
            if stack.pop() != match:
                return points[char]
    return -1



def main():

    total_score = 0
    openn = ['(','[','{','<']
    close = [')',']','}','>']

    with open('input.txt') as f:
        
        line = f.readline()

        while line:
            if not is_valid(line,openn,close):
                total_score += calc_score(line,openn,close)

            line = f.readline()

    print(f'The final score is {total_score}')


if __name__ == '__main__':
    main()