enemy_map = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5
}

def solve(enemies: str, pair_size: int)->int:
    sum = 0
    for i in range(0, len(enemies), pair_size):
        flock = enemies[i:i+pair_size]

        monsters_in_flock = 0
        for j in range(0, pair_size):
            if flock[j] == 'x':
                continue

            monsters_in_flock += 1
            sum += enemy_map[flock[j]]
        
        sum += monsters_in_flock * (monsters_in_flock - 1)

    return sum

if __name__ == '__main__':
    with open('2024/quest_1/input.txt', 'r') as f:
        print(solve(f.readline().strip(), 1))
        print(solve(f.readline().strip(), 2))
        print(solve(f.readline().strip(), 3))
