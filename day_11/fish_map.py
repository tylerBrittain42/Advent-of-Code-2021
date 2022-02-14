class MapMaker:

    # Set up stuff
    def __init__(self):
        self.mapp = []
        self.flash_count = 0
        self.day = 0

    def add_row(self, row):
        self.mapp.append(row)

    # Flashing related
    def flash(self, row, col):
        self.flash_count += 1
        width = len(self.mapp) - 1

        # diag upper left
        if row > 0 and col > 0 and self.mapp[row - 1][col - 1] != -1:
            self.mapp[row - 1][col - 1] += 1
        
        # up
        if row > 0 and self.mapp[row - 1][col] != -1:
            self.mapp[row - 1][col] += 1

        # diag upper right
        if row > 0 and col < width and self.mapp[row - 1][col + 1] != -1: 
            self.mapp[row - 1][col + 1] += 1

        # left
        if col > 0 and self.mapp[row][col - 1] != -1:
            self.mapp[row][col - 1] += 1

        # right
        if col < width and self.mapp[row][col + 1] != -1:
            self.mapp[row][col + 1] += 1

        # diag lower left
        if row < width and col > 0 and self.mapp[row + 1][col - 1] != -1:
            self.mapp[row + 1][col - 1] += 1

        # down 
        if row < width and self.mapp[row + 1][col] != -1:
            self.mapp[row + 1][col] += 1

        # diag lower right
        if row < width and col < width and self.mapp[row + 1][col + 1] != -1: 
            self.mapp[row + 1][col + 1] += 1

        return self.mapp

    def increment_step(self):
        max_flash = len(self.mapp) ** 2
        cur_flash = 0
        repeat = True

        # Incrementing all values by one
        for i,row in enumerate(self.mapp):
            for j,ele in enumerate(self.mapp):
                self.mapp[i][j] += 1
    
        # chain flashing
        while repeat:
            repeat = False
            for i,row in enumerate(self.mapp):
                for j,ele in enumerate(self.mapp):
                    if self.mapp[i][j] > 9:
                        self.mapp[i][j] = -1
                        self.flash(i,j)
                        cur_flash += 1
                        repeat = True
        
        if cur_flash == max_flash:
            print(f'All Flashed at day {self.day + 1}')
        self.day += 1


        # resetting flashed values
        for i,row in enumerate(self.mapp):
                for j,ele in enumerate(self.mapp):
                    if self.mapp[i][j] == -1:
                        self.mapp[i][j] = 0
        return self.mapp



 


    def __repr__(self):
        string_builder = ''
        for row in self.mapp:
            string_builder += ''.join(str(row)) + '\n'
        return string_builder