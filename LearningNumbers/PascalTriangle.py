from Tools.scripts.treesync import raw_input

__author__ = 'aseem'

#This program generates a Pascal Triangle
import math;


def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)));

def for_test(x,y):
    for y in range(x):
        return combination(x,y);

def pascals_triangle(rows):
    result=[];
    for count in range(rows):
        row = [];
        for element in range(count + 1):
         row.append(combination(count,element));
        result.append(row);
    return result;
num =int(raw_input("\n Enter number of rows till you want Pascal Triangle: "));
for row in pascals_triangle(num):
    print(row)
