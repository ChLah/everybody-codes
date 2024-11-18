from collections import defaultdict

def dance(cols: list[int], clapper_idx: int)->int:
    clapper = cols[clapper_idx].pop(0)
    next_col_idx = (clapper_idx+1) % len(cols)
    size = 2 * len(cols[next_col_idx])
    remainder = (clapper - 1) % size
    next_row_idx = min(remainder, size-remainder)

    cols[next_col_idx].insert(next_row_idx, clapper)

def shout(cols: list[int])->int:
    return int(''.join([str(c[0]) for c in cols]))

def parse_input(path: str)->list[int]:
    with open(path, 'r') as f:
        grid = [[int(x) for x in l.split()] for l in f.readlines()]
        #rotate so we have array of columns instead
        cols = [[r[i] for r in grid] for i in range(len(grid[0]))]
    
    return cols

def grid_to_str(grid: list[int])->str:
    return '\n'.join([' '.join([str(x) for x in row]) for row in grid])

def solve_1(grid: list[int], rounds: int)->int:
    for i in range(rounds):
        clapper_idx = i % len(grid)
        dance(grid, clapper_idx)
    
    return shout(grid)

def solve_2(grid: list[int])->int:
    seen_results = defaultdict(int)

    round = 0
    while True:
        dance(grid, round % len(grid))
        round += 1

        result = shout(grid)
        seen_results[result] = seen_results[result] + 1

        if seen_results[result] == 2024:
            return round * result

def solve_3(grid: list[int])->int:
    seen_dances = defaultdict(int)

    round = 0
    while True:
        dance(grid, round % len(grid))
        round += 1

        dance_str = grid_to_str(grid)

        if dance_str in seen_dances:
            break

        seen_dances[dance_str] = shout(grid)

    return max(seen_dances.values())
        


if __name__ == '__main__':
    print(solve_1(parse_input('2024/quest_5/input_1.txt'), 10))
    print(solve_2(parse_input('2024/quest_5/input_2.txt')))
    print(solve_3(parse_input('2024/quest_5/input_3.txt')))