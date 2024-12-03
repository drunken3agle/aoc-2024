

def read_input(file_path: str) -> (list, list):
    locations_one = []
    locations_two = []
    with open(file_path, 'r') as file:
        for line in file:
            locations_one.append(int(line.split(' ')[0].strip(' ')))
            locations_two.append(int(line.split(' ')[3].strip(' ')))

    # sort the locations
    locations_one.sort()
    locations_two.sort()
    
    return (locations_one, locations_two)

def calculate_distance(locations_one: list, locations_two: list) -> int:
    distance = 0
    for l1, l2 in zip(locations_one, locations_two):
        distance += abs(int(l1) - int(l2))
    
    return distance

def occurences(locations: list) -> dict:
    occurences = {}
    for location in locations:
        if location in occurences:
            occurences[location] += 1
        else:
            occurences[location] = 1
    
    return occurences

def calculate_similarity(locations: list, occurences: dict) -> int:
    similarity = 0
    for location in locations:
        if location in occurences:
            similarity += occurences[location] * location
    
    return similarity

if __name__ == '__main__':
    ls1, ls2 = read_input('inputs/day_one.txt')
    print(f'Part 1: {calculate_distance(ls1, ls2)}')
    print(f'Part 2: {calculate_similarity(ls1, occurences(ls2))}')