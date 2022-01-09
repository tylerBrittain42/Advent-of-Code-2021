import part_1 as p1
import part_2 as p2


valid = ['([])','{()()()}','<([{}])>','[<>({}){}[([])<>]]','(((((((((())))))))))']
invalid = ['{([(<{}[<>[]}>{[]{[(<()>','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{']
incomplete = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','(((({<>}<{<{<>}{[]{[]{}','{<[[]]>}<{[{[{[]{()[[[]','<{([{{}}[<[[[<>{}]]]>[]]']
incomplete_remainder = ['}}]])})]',')}>]})','}}>}>))))',']]}}]}]}>','])}>']
incomplete_points = [288957, 5566, 1480781, 995444, 294]

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
        

def test_calc_invalid():

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
        assert len(p2.is_complete(seq,open,close)) == 0
    for seq in incomplete:
        assert len(p2.is_complete(seq,open,close)) > 0

def test_calc_complete():

    open = ['(','[','{','<']
    close = [')',']','}','>']

    for i, seq in enumerate(incomplete):
        print('fuck')
        assert p2.calc_score(p2.is_complete(seq,open,close)) == incomplete_points[i]



