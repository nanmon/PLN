#!/usr/bin/env python
# encoding: UTF-8

def minimum_edit_distance(w1, w2):
    matrix = [
        [
            {
                "cost": j if i == 0 else i if j == 0 else 0,
                "up": j == 0 and i != 0,
                "left": i == 0 and j != 0,
                "corner": False
            }
        for j in range(len(w2) + 1) ] 
    for i in range(len(w1) + 1) ]

    for i in range(1, len(w1) + 1):
        for j in range(1, len(w2) + 1):
            up_cost = matrix[i-1][j]["cost"] + 1
            left_cost = matrix[i][j-1]["cost"] + 1
            corner_cost = matrix[i-1][j-1]["cost"]
            if w1[i-1] != w2[j-1]:
                corner_cost += 2
            min_cost = min([up_cost, left_cost, corner_cost])
            matrix[i][j] = {
                "cost": min_cost,
                "up": up_cost == min_cost,
                "left": left_cost == min_cost,
                "corner": corner_cost == min_cost
            }
    return matrix

def cell_to_string(cell):
    val = str(cell["cost"])
    val += 'u' if cell["up"] else ' '
    val += "l" if cell["left"] else ' '
    val += "c" if cell["corner"] else ' '
    return val
    
def print_fitting(w1, w2, matrix):
    i, j = len(w1), len(w2)
    new_w1 = w1
    new_w2 = w2
    while i != 0 or j != 0:
        left_cost = len(w1) + len(w2)
        if matrix[i][j]["left"]:
            left_cost = matrix[i][j-1]["cost"] 
        up_cost = len(w1) + len(w2)
        if matrix[i][j]["up"]:
            up_cost = matrix[i-1][j]["cost"]
        corner_cost = len(w1) + len(w2)
        if matrix[i][j]["corner"]:
            corner_cost = matrix[i-1][j-1]["cost"]
        if left_cost < corner_cost:
            new_w1 = new_w1[:i] + '*' + new_w1[i:]
            j -= 1
        elif up_cost < corner_cost:
            new_w2 = new_w2[:j] + '*' + new_w2[j:]
            i -= 1
        else:
            i -= 1
            j -= 1
    print(new_w1)
    print(new_w2)
        

def main():
    w1, w2 = input("Primera cadena: "), input('Segunda cadena: ')
    result = minimum_edit_distance(w1, w2)
    for row in result:
        print([ cell_to_string(cell) for cell in row])
    print_fitting(w1, w2, result)

if __name__ == '__main__':
    main()