
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# general description

The project contains separate functions for calculating the area and perimeter of shapes: circle, square, triangle. It also contains the "calculator" function needed to dynamically calculate the perimeter or area of geometric shapes.

# Description of each function with call examples

1. circle.py
`The function takes one arguments: r (the radius of the circle) and returns math.pi * r * r (the area of the circle)`
`Input example: r=10, returned 314.1592653589793`
def area(r):
    return math.pi * r * r

`The function takes one arguments: r (the radius of the circle) and returns 2 * math.pi * r (the perimeter of the circle)`
`Input example: r=10, returned 62.83185307179586`
def perimeter(r):
    return 2 * math.pi * r
//Принимает рвдиус круга = r, возвращает его периметр

2. square.py
`The function takes one arguments: a (the side of the square) and returns a * a (the area of the square)`
`Input example: r=10, returned 20`
def area(a):
    return a * a

`The function takes one arguments: a (the side of the square) and returns 4 * a (the perimeter of the square)`
`Input example: r=10, returned 40`
def perimeter(a):
    return 4 * a

3. triangle.py
`The function takes three variables: a,b,c (the side of the triangle), counts the perimeter/2 and returns sqrt(p * (p-a) * (p-b) * (p-c)) (the area of the triangle)`
`Input example: a=3, b=4, c=5, returned 6`
def area(a, b, c):
    p=(a+b+c)/2
    return sqrt(p * (p-a) * (p-b) * (p-c))

`The function takes three arguments: a,b,c (the side of the triangle) and returns a+b+c (the perimeter of the triangle)`
`Input example: a=3, b=4, c=5, returned 12`
def perimeter(a, b, c):
    return a + b + c

4. calcilate.py
`The function takes three arguments: <fig> (The name of the geometric shape), <func> (The name of the operation), <size> (A list of the dimensions of the shape). `
`Then assert fig in figs: Checking that the passed shape name is in the list of valid figures. assert func in functions: Checking that the passed operation name is in the list of valid functions result = eval(f'{fig}.{func}(*{size})'): The eval function is used to calculate the result. f'{fig}.{func}(*{size})' is an f-string that forms a string with the function call code. print(f'{func} of {fig} is {result}'): Outputs the result of calculations to the console `
`Input example: fig = 'circle', func = 'perimeter', and size = [5], returned: perimeter of circle is 31.41592653589793'`
figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

# history of project changes with commit hashes (except the last entry)
- 00d4fd8b996a228a8c2393c3001551f8010b3b6c (HEAD -> Documentation) Added a description of the functions in the files, fixed an error in the file triangle.py
- b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop, develop) L-04: Update docs for calculate.py
- d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71 L-04: Add calculate.py
- 51c40ebfd0e0b65f52fe5e54740cbb038e492db3 L-04: Doc updated for triangle
- d080c7888b81955bad2ed78d58ad910526b5132a L-04: Triangle added
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main) L-03: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 Circle and square added
