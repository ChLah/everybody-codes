def solve_1(lines: list[str])->str:
    solution = ""

    for l in range(len(lines)):
        lineset = set(lines[l])

        for c in range(len(lines[l])):
            if lines[l][c] != '.':
                continue

            colset = set([lines[r][c] for r in range(len(lines)) if not lines[r][c] in ['.', '*']])
            solution += lineset.intersection(colset).pop()
    
    return solution

def solve_2(lines: list[str])->int:
    big_rows = [lines[i:i+8] for i in range(0,len(lines),9)]
    big_row = list(map(" ".join,zip(*big_rows)))
    big_row = [l.split() for l in big_row]
    grids = list(zip(*big_row))

    score = 0
    for grid in grids:
        word = solve_1(grid)
        score += sum(idx * (ord(char)-64) for idx,char in enumerate(word,1))

    return score



if __name__ == "__main__":
    with open('2024/quest_10/input_1.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        #print(solve_1(lines))
    
    with open('2024/quest_10/input_2.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve_2(lines))

    
    
