def find_all(sentence: str, word: str, with_overlap: bool = False):
    extended_sentence = sentence + sentence if with_overlap else sentence
    word_len = len(word)
    sentence_len = len(sentence)
    
    for i in range(sentence_len):
        if extended_sentence[i:i + word_len] == word:
            yield i

def replace_in(sentence: str, idx: int, count: int)->str:
    response = sentence

    for i in range(count):
        effective_idx = (idx + i) % len(response)
        response = response[:effective_idx] + 'x' + response[effective_idx+1:]

    return response

def solve_1(words: list[str], sentence: str)->int:
    return sum([sentence.count(word) for word in words])

def solve_2(words: list[str], lines: list[str])->tuple[int, list[str]]:
    # add words in reverse
    words.extend([x[::-1] for x in words])

    new_lines = []
    for sentence in lines:
        new_sentence = sentence
        for word in words:
            for occurence_idx in find_all(sentence, word):
                new_sentence = replace_in(new_sentence, occurence_idx, len(word))
        
        new_lines.append(new_sentence)

    count = sum([line.count('x') for line in new_lines])

    return count, new_lines

def solve_3(words: list[str], lines: list[str])->int:
    # add words in reverse
    words.extend([x[::-1] for x in words])
    
    new_lines = solve_2(words, lines)[1]
    
    for i in range(len(lines[0])):
        sentence = ''.join([l[i] for l in lines])
        for word in words:
            for occurence_idx in find_all(sentence, word, False):
                for j in range(len(word)):
                    effective_line_idx = (occurence_idx + j) % len(sentence)
                    # Modify the existing line array accordingly
                    # Since we need the effective line idx, we need to do the loop here ourself
                    new_lines[effective_line_idx] = replace_in(new_lines[effective_line_idx], i, 1)

    return sum([line.count('x') for line in new_lines])

if __name__ == '__main__':
    with open('2024/quest_2/input_1.txt', 'r') as f:
        words = f.readline().strip()[6:].split(',')
        sentence = f.readline().strip()
        print(solve_1(words, sentence))
        
    with open('2024/quest_2/input_2.txt', 'r') as f:
        words = f.readline().strip()[6:].split(',')
        sentences = [x.strip() for x in f.readlines()]
        print(solve_2(words, sentences)[0])
    
    with open('2024/quest_2/input_3.txt', 'r') as f:
        words = f.readline().strip()[6:].split(',')
        sentences = [x.strip() for x in f.readlines()]
        print(solve_3(words, sentences))
