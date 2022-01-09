import part_1 as p1
import part_2 as p2


valid = ['([])','{()()()}','<([{}])>','[<>({}){}[([])<>]]','(((((((((())))))))))']
invalid = ['{([(<{}[<>[]}>{[]{[(<()>','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{']
incomplete = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','(((({<>}<{<{<>}{[]{[]{}','{<[[]]>}<{[{[{[]{()[[[]','<{([{{}}[<[[[<>{}]]]>[]]']

#### Part One Tests ####
 
def test_stack():
    test_stack = p1.Stack()
    for i in range(0,5):
        test_stack.add(i)
        assert test_stack.peek() == i
    assert test_stack.pop() == 4
    

def test_is_valid():

    open = ['(','[','{','<']
    close = [')',']','}','>']

    for seq in valid:
        assert p1.is_valid(seq,open,close) == True
    for seq in invalid:
        assert p1.is_valid(seq,open,close) == False
        

def test_calc():

    open = ['(','[','{','<']
    close = [')',']','}','>']
    sum = 0
    
    for seq in invalid:
        sum += p1.calc_score(seq,open,close)
    assert sum == 26397

#### Part Two Tests ####

def test_is_complete():

    open = ['(','[','{','<']
    close = [')',']','}','>']

    for seq in valid:
        assert p2.is_complete(seq,open,close) == True
    for seq in invalid:
        assert p2.is_complete(seq,open,close) == False
