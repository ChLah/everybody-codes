def solve(nails: list[int])->int:
    shortest = min(nails)
    return sum([n - shortest for n in nails])

def solve_3(nails: list[int])->int:
    nails.sort()
    mean = nails[len(nails) // 2]
    return sum([abs(n - mean) for n in nails])

if __name__ == '__main__':
    with open('2024/quest_4/input_1.txt', 'r') as f:
        nails = [int(l) for l in f.readlines()]
        print(solve(nails))
    
    with open('2024/quest_4/input_2.txt', 'r') as f:
        nails = [int(l) for l in f.readlines()]
        print(solve(nails))
    
    with open('2024/quest_4/input_3.txt', 'r') as f:
        nails = [int(l) for l in f.readlines()]
        print(solve_3(nails))