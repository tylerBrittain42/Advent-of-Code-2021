
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

# assuming a stack is valid
def is_complete(sequence, openn, close):

    stack = Stack()

    for char in sequence:
        if char in openn:
            stack.add(char)
        elif char in close:
            stack.pop()

    return stack.stack
    


def calc_score(sequence):

    total = 0
    points = { '(':1, '[':2, '{':3, '<':4 }
    
    sequence.reverse()

    for i in sequence:
        total = 5*total +  points[i]
    return total



def main():

    scores = []
    openn = ['(','[','{','<']
    close = [')',']','}','>']
    valid_seq = []

    with open('input.txt') as f:
        
        line = f.readline()

        # filtering for valid lines
        while line:
            if is_valid(line,openn,close):
                valid_seq.append(line)
            line = f.readline()

        # checking valid lines for completeness
        for seq in valid_seq:
            complete_seq = is_complete(seq,openn,close)
            if len(complete_seq) != 0:
                scores.append(calc_score(complete_seq))

        # Grabbing median score
        scores.sort()
        final_score = scores[int(len(scores)/2)]    

    print(f'The middle score is {final_score}')


if __name__ == '__main__':
    main()