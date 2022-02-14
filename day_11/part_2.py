import fish_map

def main():



    # creates initial 2d array
    fish = fish_map.MapMaker()

    with open('input.txt') as f:
        for line in f:
            row = []
            for char in line.rstrip('\n'):
                row.append(int(char))
            fish.add_row(row)

    for i in range(500):
        fish.increment_step()
    print(f'There have been a total of {fish.flash_count} flashes')
    




if __name__ == '__main__':
    main()