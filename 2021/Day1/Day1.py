
with open(r'C:\Projekt\Python\AdventCode\2021\Day1\sonar_report.txt') as f:
    lines = f.readlines()

# Uppg. 1
def check_if_increased():
    prev = lines[0]
    increases = 0
    for line in lines:
        if line > prev:
            increases = increases+1
        prev = line
    return increases

# Uppg. 2
def check_three_vals():
    increases = 0
    line_counter = 0
    total = 0
    prev_total = 0
    for line in lines:
        if line_counter < (len(lines)-(len(lines)%3)):
            total = int(lines[line_counter]) + int(lines[line_counter+1]) + int(lines[line_counter+2])
        if total > prev_total and prev_total is not 0:
            increases = increases + 1
        prev_total = total
        line_counter = line_counter + 1
    return increases


if __name__ == '__main__':
    print(check_if_increased()+1) # Borde inte vara "+1"?
    print(check_three_vals())