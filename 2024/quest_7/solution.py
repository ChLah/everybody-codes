def solve_1(lines: list[str])->str:
    scores = dict()

    for line in lines:
        [name, instructions] = line.split(':')
        instructions = instructions.split(',')

        score = 0
        power = 10

        for round in range(10):
            instr = instructions[round%len(instructions)]

            if instr == '+':
                power += 1
            elif instr == '-' and power > 0:
                power -= 1
            
            score += power
                
        scores[name] = score
    
    return ''.join([name for name in sorted(scores, key=lambda x: scores[x], reverse=True)])

def solve_2(lines: list[str], track: str)->str:
    scores = dict()

    for line in lines:
        [name, instructions] = line.split(':')
        instructions = instructions.split(',')

        score = 0
        power = 10

        i = 0
        for _ in range(10):
            for instr in track:
                if instr == '=':
                    instr = instructions[i%len(instructions)]

                if instr == '+':
                    power += 1
                elif instr == '-' and power > 0:
                    power -= 1
                
                i += 1
                score += power
                
        scores[name] = score
    
    return ''.join([name for name in sorted(scores, key=lambda x: scores[x], reverse=True)])  

def build_trackstr(lines: list[str])->str:
    resp = ''

    resp += lines[0][1:] # strip the S from the start to begin with first instruction
    resp += ''.join([line[-1] for line in lines[1:-1]]) # get the last instruction of each line
    resp += lines[-1][::-1] # reverse the last line
    resp += ''.join(reversed([line[0] for line in lines[0:-1]])) # get the first instruction of each line in reverse order including the first line

    return resp

if __name__ == '__main__':
    with open('2024/quest_7/input_1.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve_1(lines))
    
    with open('2024/quest_7/track.txt', 'r') as f:
         track = build_trackstr([l.strip() for l in f.readlines()])

    with open('2024/quest_7/input_2.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve_2(lines, track))