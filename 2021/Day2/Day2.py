with open(r'C:\Projekt\Python\AdventCode\2021\Day2\planned_course.txt') as f:
    lines = f.readlines()

# Part 1
def part_one():
    depth = 0
    horizontal = 0

    for line in lines:
        split = line.split(" ")
        if split[0] == 'up':
            depth = depth - int(split[1])
        elif split[0] == 'down':
            depth = depth + int(split[1])
        elif split[0] == 'forward':
            horizontal = horizontal + int(split[1])
    
    return depth * horizontal

def part_two():
    depth = 0
    horizontal = 0
    aim = 0

    for line in lines:
        split = line.split(" ")
        if split[0] == 'up':
            aim = aim - int(split[1])
        elif split[0] == 'down':
            aim = aim + int(split[1])
        elif split[0] == 'forward':
            horizontal = horizontal + int(split[1])
            depth = depth + aim * int(split[1])
    
    return depth * horizontal


if __name__ == '__main__':
    print(part_one())
    print(part_two())
