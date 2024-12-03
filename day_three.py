import re

if __name__ == '__main__':
    with open('inputs/day_three.txt', 'r') as f:
        data = f.read()

    multiplications = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    
    activations = re.compile(r"do\(\)|don't\(\)") # there is no try
    
    result = 0
    previous_match = None
    for match in activations.finditer(data):
        if previous_match is None or previous_match.group() == 'do()':
            start = 0 if previous_match is None else previous_match.end()
            result += sum([ int(mul[0]) * int(mul[1]) for mul in multiplications.findall(data[start:match.start()]) ])
            
        previous_match = match
        
    print(f'Part 1: {sum([ int(match[0]) * int(match[1]) for match in multiplications.findall(data) ])}')
    print(f'Part 2: {result}')
