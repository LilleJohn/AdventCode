with open(r'C:\Projekt\Python\AdventCode\2020\Day3\map.txt') as f:
    lines = f.readlines()

row, column, width = 0, 0, len(lines[0])-1

def check_trees(x, y, row, column, width):
    trees = 0
    for line in lines:
        if column >= width:
            column = column-width
        if row > len(lines):
            break
        if lines[row][column] == '#':
            trees = trees+1
        row = row+y
        column = column+x
    return trees

if __name__ == '__main__':
    # Part 1
    print("Part 1:", check_trees(3, 1, row, column, width))

    # Part 2
    vars = []
    vars.append(check_trees(1, 1, row, column, width))
    vars.append(check_trees(3, 1, row, column, width))
    vars.append(check_trees(5, 1, row, column, width))
    vars.append(check_trees(7, 1, row, column, width))
    vars.append(check_trees(1, 2, row, column, width))
    vars.append(vars[0]*vars[1]*vars[2]*vars[3]*vars[4])
    print("Part 2:", vars[5])