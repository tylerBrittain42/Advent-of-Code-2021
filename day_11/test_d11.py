import fish_map

### Mapp Object tests

def test_init_creation():
    mapp = fish_map.MapMaker()
    mapp.add_row('123')
    mapp.add_row('456')
    mapp.add_row('789')
    assert str(mapp) =='123\n456\n789\n' 

def test_flashing():
    mapp = fish_map.MapMaker()

    # upper left
    mapp.mapp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert mapp.flash(0,0) == [[0,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]

    # center
    mapp.mapp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert mapp.flash(1,1) == [[1,1,1,0],[1,0,1,0],[1,1,1,0],[0,0,0,0]]

    # lower right
    mapp.mapp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert mapp.flash(3,3) == [[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,1,0]]


def test_single_step():
    mapp = fish_map.MapMaker()

    # Step(no flashing)
    mapp.mapp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert mapp.increment_step() == [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]


    mapp.mapp = [[0,0,0,0],[0,9,0,0],[0,0,0,0],[0,0,0,0]]
    assert mapp.increment_step() == [[2,2,2,1],[2,0,2,1],[2,2,2,1],[1,1,1,1]]



    # Step (some flashing)
    mapp.mapp = [[10,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,10]]
    assert mapp.increment_step() == [[0,2,1,1],[2,2,1,1],[1,1,2,2],[1,1,2,0]]

    mapp.mapp = []
    # Flashing from example
    with open('t_input.txt') as f:
        for line in f:
            row = []
            for char in line.rstrip('\n'):
                row.append(int(char))
            mapp.add_row(row)
    assert mapp.increment_step() == [[3,4,5,4,3],[4,0,0,0,4],[5,0,0,0,5],[4,0,0,0,4],[3,4,5,4,3]]


def test_aoc_examples():

    mapp = fish_map.MapMaker()
    with open('t_example.txt') as f:
        for line in f:
            row = []
            for char in line.rstrip('\n'):
                row.append(int(char))
            mapp.add_row(row)

    for i in range(100):
        mapp.increment_step()
    assert mapp.flash_count == 1656