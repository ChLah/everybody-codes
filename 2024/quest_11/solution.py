from collections import Counter

def parse_rules(lines: list[str])->dict:
    rules = {}
    for line in lines:
        rule, values = line.split(':')
        values = values.split(',')
        rules[rule] = values

    return rules

def simulate(rules: dict, start: str, rounds: int)->int:
    counts = Counter({start: 1})

    for _ in range(rounds):
        new_counts = Counter()

        for rule, count in counts.items():
            for value in rules[rule]:
                new_counts[value] += count

        counts = new_counts
    
    return sum(counts.values())

def solve_1(lines: list[str])->int:
    rules = parse_rules(lines)
    return simulate(rules, 'A', 4)

def solve_2(lines: list[str])->int:
    rules = parse_rules(lines)
    return simulate(rules, 'Z', 10)

def solve_3(lines: list[str])->int:
    rules = parse_rules(lines)
    populations = list([simulate(rules, x, 20) for x in rules.keys()])
    
    return max(populations) - min(populations)


if __name__ == "__main__":
    with open('2024/quest_11/input_1.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve_1(lines))

    with open('2024/quest_11/input_2.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve_2(lines))

    with open('2024/quest_11/input_3.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve_3(lines))
    
    
