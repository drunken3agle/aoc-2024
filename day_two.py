def read_input(file_path: str) -> list:
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append([int(x) for x in line.split(' ')])
            
    return reports

def analyze_report(report: list) -> int:
    is_ascending = report[0] < report[1]
    for i in range(len(report) - 1):
        if (report[i] <= report[i + 1]) != is_ascending:
            return 0
        
        if (abs(report[i] - report[i + 1]) > 3) or (report[i] == report[i + 1]):
            return 0
    
    return 1

def recheck_report(report: list) -> int:
    for i in range(len(report)):
        tmp_report = report.copy()
        tmp_report.pop(i)
        if analyze_report(tmp_report) == 1:
            return 1
        
    return 0
    
def also_analyze_report(report: list) -> int:    
    diffs = [report[i] - report[i + 1] for i in range(len(report)- 1)]
    all_same_sign = all([diff < 0 for diff in diffs]) or all([diff > 0 for diff in diffs])
    if not all_same_sign:
        return 0
    
    if any([abs(diff) > 3 for diff in diffs]) or any([diff == 0 for diff in diffs]):
        return 0
    
    return 1

if __name__ == '__main__':
    reports = read_input('inputs/day_two.txt')
    
    intially_unsafe = [report for report in reports if analyze_report(report) == 0]
    additionally_safe = sum([recheck_report(report) for report in intially_unsafe])
    
    print(f'Part 1: {sum([analyze_report(report) for report in reports])}')
    print(f'Part 2: {len(reports) - len(intially_unsafe) + additionally_safe}')