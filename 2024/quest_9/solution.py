def get_min_counts(max_val: int, stamps: list[int])->list[int]:
    min_counts = [max_val+1] * (max_val+1) # initialize array with maximum count needed
    min_counts[0] = 0

    for amount in range(1, max_val+1):
        for stamp in stamps:
            if amount >= stamp:
                min_counts[amount] = min(min_counts[amount], min_counts[amount-stamp]+1)
    
    return min_counts

def solve_simple(numbers: list[int], stamps: list[int])->int:
    min_counts = get_min_counts(max(numbers), stamps)
    return sum([min_counts[n] for n in numbers])

def solve_1(numbers: list[int])->int:
    return solve_simple(numbers, [10,5,3,1])

def solve_2(numbers: list[int])->int:
    return solve_simple(numbers, [30,25,24,20,16,15,10,5,3,1])

def solve_3(numbers: list[int])->int:
    min_counts = get_min_counts(max(numbers), [101,100,75,74,50,49,38,37,30,25,24,20,16,15,10,5,3,1])
    count = 0

    for n in numbers:
        half = n // 2
        remainder = n - half
        min_val = float('inf')

        while abs(half - remainder) <= 100:
            min_val = min(min_val, min_counts[half] + min_counts[remainder])
            half -= 1
            remainder += 1
        
        count += min_val

    return count


if __name__ == "__main__":
    with open('2024/quest_9/input_1.txt', 'r') as f:
        numbers = [int(l.strip()) for l in f.readlines()]
        print(solve_1(numbers))

    with open('2024/quest_9/input_2.txt', 'r') as f:
        numbers = [int(l.strip()) for l in f.readlines()]
        print(solve_2(numbers))

    with open('2024/quest_9/input_3.txt', 'r') as f:
        numbers = [int(l.strip()) for l in f.readlines()]
        print(solve_3(numbers))
    
