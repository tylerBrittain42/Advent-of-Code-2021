class gameBoard:

    def __init__(self):
        self.rows = []
        self.bool_rows = []
        self.score = -1
    
    def add_row(self, new_row):
        self.rows.append(new_row)
        new_bool = [False] * len(new_row)
        self.bool_rows.append(new_bool)

    def add_ans(self,ans):
        for i,row in enumerate(self.rows):
            for j,ele in enumerate(row):
                if ele == ans:
                    self.bool_rows[i][j] = True

    def row_count(self):
        return len(self.rows)


    def layout(self, type) -> str:
        if type == 'b':
            return str(self.bool_rows) 
        if type == 'c':
            return str(self.rows)

    def isWin(self):
        # row win
        for i,row in enumerate(self.bool_rows):
            if row.count(row[0]) == len(row) and row[0] == True:
                return True
        
        # col win
        for i in range(0,len(self.bool_rows[0])):
            match_count = 0
            for j in range(0,len(self.bool_rows)):
                if self.bool_rows[j][i] == True:
                    match_count += 1
            if match_count == len(self.bool_rows[0]):
                return True

        # no win
        return False

    def calc_score(self,ans):
        score = 0
        for i, row in enumerate(self.bool_rows):
            for j, ele in enumerate(row):
                if ele == False:
                    score += int(self.rows[i][j])
        return score * int(ans)

def main():

    boards = []
    new_board = gameBoard()

    # Creating the boards
    with open('input.txt') as f:
        winning_sequence = f.readline().split(',')

        # newline between key and boards
        line = f.readline()
        line = f.readline().rstrip()

        while (line):

            line = line.rstrip('\n')

            if line == '':
                boards.append(new_board)
                new_board = gameBoard()

            else:
                new_row = line.split(' ')
                while('' in new_row):
                    new_row.remove('')
                new_board.add_row(new_row)
            
            line = f.readline()

        boards.append(new_board)

    # Checking the boards for a bingo
    last_win = None
    last_ans = None
    has_won = []
    for ans in winning_sequence:
        for i, board in enumerate(boards):
            board.add_ans(ans.rstrip('\n'))
            if board.isWin():
                if i not in has_won:
                    has_won.append(i)
                    last_win = i
                    last_ans = ans
                    board.score = board.calc_score(ans)
                    print(f'Board {i} WON')
                    print(f'{board.score}')
                    
    print(f'The last winner is {last_win} with a score of {boards[last_win].score}')
    

        


if __name__ == "__main__":
    main()


