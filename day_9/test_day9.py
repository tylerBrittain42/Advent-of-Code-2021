import part_2 as p

map = [
[2,1,9,9,9,4,3,2,1,0],
[3,9,8,7,8,9,4,9,2,1],
[9,8,5,6,7,8,9,8,9,2],
[8,7,6,7,8,9,6,7,8,9],
[9,8,9,9,9,6,5,6,7,8]
]

def test_explore():

    # corner
    assert p.explore(map,0,0) == [[0,1],[1,0]]
    # default
    assert p.explore(map,1,1) == [[0,1],[1,2],[2,1],[1,0]]
    # upper
    assert p.explore(map,0,1) == [[0,2],[1,1],[0,0]]
    # lower
    assert p.explore(map,4,1) == [[3,1],[4,2],[4,0]]
    # left
    assert p.explore(map,1,0) == [[0,0],[1,1],[2,0]]
    # right
    assert p.explore(map,1,9) == [[0,9],[2,9],[1,8]]