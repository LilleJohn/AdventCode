import re

with open(r'C:\Projekt\Python\AdventCode\2020\Day4\passports.txt') as f:
    lines = f.readlines()

check_for_nocid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
check_for_cid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
#print(lines[2]) #debug

def check_passports(check_for):
    row, valid_param, valid_passp = 0, 0, 0
    vars, vars_temp = [], []
    for line in lines:
        if len(lines[row]) > 1:
            vars_temp = re.split(' |:', lines[row])
            for i in range(len(vars_temp)):
                vars.append(vars_temp[i])
        else:
            for i in range(len(check_for)):
                if check_for[i] in vars:
                    valid_param = valid_param+1
                if valid_param == len(check_for):
                    valid_passp = valid_passp+1
                    valid_param = 0
            vars, vars_temp = [], []
        row = row+1
    return valid_passp


if __name__ == '__main__':
    print(check_passports(check_for_nocid))
