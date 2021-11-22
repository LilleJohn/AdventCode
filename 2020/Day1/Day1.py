with open(r'C:\Projekt\Python\AdventCode\2020\Day1\expense_report.txt') as f:
    lines = f.readlines()

def part_one():
    for first in lines:
        for second in lines:
            if int(first) + int(second) == 2020:
                return(int(first)*int(second))

def part_two():
    for first in lines:
        for second in lines:
            for third in lines:
                if int(first) + int(second) + int(third) == 2020:
                    return(int(first)*int(second)*int(third))

if __name__ == '__main__':
    print("Part 1:", part_one())
    print("Part 2:", part_two())
