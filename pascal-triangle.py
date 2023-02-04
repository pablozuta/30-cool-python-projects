'''
This Python project prints out Pascal’s Triangle by utilizing conditional statements and loops. It also uses the standard library’s math module and factorial function to evaluate the number of combinations equation used to generate the values in the triangle.
'''

from math import factorial

def pascal_triangle(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(end= ' ')

        for j in range(i + 1):

            print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')    
        print()


if __name__ == '__main__':
    pascal_triangle(5)