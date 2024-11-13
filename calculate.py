import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
    "perimeter-square": 1,
    "area-triangle": 3,
    "perimeter-triangle": 3
}

def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    if any(s <= 0 for s in size):
        raise ValueError("The dimensions of the figure must be greater than zero")

    expected_size = sizes.get(f"{func}-{fig}")
    if len(size) != expected_size:
        raise ValueError(f"{expected_size} parameters are expected for {fig} and the function {func}")

    if fig == 'triangle':
        if size[0] + size[1] <= size[2] or size[0] + size[2] <= size[1] or size[1] + size[2] <= size[0]:
            raise ValueError("Incorrect dimensions for the triangle")

    result = eval(f"{fig}.{func}(*{size})")
    return result

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while True:
        size = list(map(int, input(f"Input {sizes.get(f'{func}-{fig}', 1)} figure sizes separated by space: \n").split(' ')))
        try:
            result = calc(fig, func, size)
            break
        except ValueError as e:
            print(e)

    print(f'{func} of {fig} is {result}')