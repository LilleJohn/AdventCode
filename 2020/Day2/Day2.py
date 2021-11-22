import re

with open(r'C:\Projekt\Python\AdventCode\2020\Day2\passwords.txt') as f:
    lines = f.readlines()

def part_one():
    valid_passwords = 0
    for line in lines:
        vars = re.split('-| |: ', line)
        letters_exists = 0
        for letters in vars[3]:
            if letters == vars[2]:
                letters_exists = letters_exists+1
        if int(vars[0]) <= letters_exists <= int(vars[1]):
            valid_passwords = valid_passwords+1
    return(valid_passwords)

def part_two():
    valid_passwords = 0
    for line in lines:
        vars = re.split('-| |: ', line)
        if vars[3][int(vars[0])] == vars[2] and vars[3][int(vars[1])] != vars[2]:
            valid_passwords = valid_passwords+1
        if vars[3][int(vars[1])] == vars[2] and vars[3][int(vars[0])] != vars[2]:
            valid_passwords = valid_passwords+1
    return(valid_passwords)


if __name__ == '__main__':
    print("Part 1:", part_one())
    print("Part 2:", part_two())
