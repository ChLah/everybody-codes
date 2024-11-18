from collections import defaultdict, deque

def bfs(node_dict: dict[str, list[str]]) -> list[str]:
    to_check = deque([["RR"]])
    paths_by_lengths = defaultdict(list)

    while to_check:
        path = to_check.popleft()
        key = path[-1]

        if key == "@":
            paths_by_lengths[len(path)].append(path)

        if key in {"BUG", "ANT"} or key not in node_dict:
            continue

        children = node_dict[key]
        for c in children:
            to_check.append(path + [c])
    
    for path in paths_by_lengths.values():
        if len(path) == 1:
            return path.pop()
        
    # Should never happen since there is always a single path with unique length
    return []

def build_tree_dict(lines: str)->dict[str, list[str]]:
    node_dict = dict()
    for line in lines:
        [node_name, paths] = line.split(':')
        node_dict[node_name] = paths.split(',')
    
    return node_dict

def solve(lines: str, use_first: bool = False)->str:
    tree_dict = build_tree_dict(lines)
    result = bfs(tree_dict)

    return ''.join([c[0] if use_first else c for c in result])

if __name__ == '__main__':
    with open('2024/quest_6/input_1.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve(lines))
    
    with open('2024/quest_6/input_2.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve(lines, True))
    
    with open('2024/quest_6/input_3.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(solve(lines, True))