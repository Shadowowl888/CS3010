import math

# x^2 - y^2 = 49
def solve_equation():
    solutions = []
    for x in range(-100, 101):  # Iterating through possible values of x
        for y in range(-100, 101):  # Iterating through possible values of y
            if x**2 - y**2 == 49:  # Checking if the equation holds true
                solutions.append((x, y))
    return solutions

# x = sin(x)
def fixed_point_iteration1(initial_guess, tolerance, max_iterations):
    x_prev = initial_guess
    for i in range(max_iterations):
        x_next = math.sin(x_prev)
        if abs(x_next - x_prev) < tolerance:
            return x_next
        x_prev = x_next
    return None  # Solution not found within max_iterations

# x = sin(x + pi/4)
def fixed_point_iteration2(initial_guess, tolerance, max_iterations):
    x_prev = initial_guess
    for i in range(max_iterations):
        x_next = math.sin(x_prev + (math.pi / 4.0))
        if abs(x_next - x_prev) < tolerance:
            return x_next
        x_prev = x_next
    return None  # Solution not found within max_iterations

# x = log(x+1)
def fixed_point_iteration3(initial_guess, tolerance, max_iterations):
    x_prev = initial_guess
    for i in range(max_iterations):
        x_next = math.log10(x_prev + 1)
        if abs(x_next - x_prev) < tolerance:
            return x_next
        x_prev = x_next
    return None  # Solution not found within max_iterations

# x = log(x) + 1
def fixed_point_iteration4(initial_guess, tolerance, max_iterations):
    x_prev = initial_guess
    for i in range(max_iterations):
        x_next = math.log10(x_prev) + 1
        if abs(x_next - x_prev) < tolerance:
            return x_next
        x_prev = x_next
    return None  # Solution not found within max_iterations

# x = log(x) - 1
# def fixed_point_iteration5(initial_guess, tolerance, max_iterations):
#     x_prev = initial_guess
#     for i in range(max_iterations):
#         x_next = math.log10(x_prev) - 1
#         if abs(x_next - x_prev) < tolerance:
#             return x_next
#         x_prev = x_next
#     return None  # Solution not found within max_iterations

# e^-x / (e - 1)
def fixed_point_iteration6(initial_guess, tolerance, max_iterations):
    global e
    x_prev = initial_guess
    for i in range(max_iterations):
        x_next = (e ** (-x_prev)) / (e - 1)
        if abs(x_next - x_prev) < tolerance:
            return x_next
        x_prev = x_next
    return None  # Solution not found within max_iterations

def main():
    global e
    e = math.exp(1)      # Euler's number
    initial_guess = 1.0  # Initial guess
    tolerance = 1e-8     # Tolerance for convergence
    max_iterations = 1000000  # Maximum number of iterations

    # x^2 - y^2 = 49
    solutions = solve_equation()
    print("Solutions for x^2 - y^2 = 49:")
    for solution in solutions:
        print(f"x = {solution[0]}, y = {solution[1]}")

    # x = sin(x)
    solution = fixed_point_iteration1(initial_guess, tolerance, max_iterations)
    if solution is not None:
        print("Solution found x=sin(x):", solution)
    else:
        print("Solution not found within max iterations.")

    # x = sin(x + pi/4)
    solution = fixed_point_iteration2(initial_guess, tolerance, max_iterations)
    if solution is not None:
        print("Solution found x=sin(x + pi/4):", solution)
    else:
        print("Solution not found within max iterations.")

    # x = log(x+1)
    solution = fixed_point_iteration3(initial_guess, tolerance, max_iterations)
    if solution is not None:
        print("Solution found x=log(x + 1):", solution)
    else:
        print("Solution not found within max iterations.")

    # x = log(x) + 1
    solution = fixed_point_iteration4(initial_guess, tolerance, max_iterations)
    if solution is not None:
        print("Solution found x=log(x) + 1:", solution)
    else:
        print("Solution not found within max iterations.")

    # x = log(x) - 1
    # solution = fixed_point_iteration5(initial_guess, tolerance, max_iterations)
    # if solution is not None:
    #     print("Solution found x=log(x) - 1:", solution)
    # else:
    #     print("Solution not found within max iterations.")

    # e^-x / (e - 1)
    solution = fixed_point_iteration6(initial_guess, tolerance, max_iterations)
    if solution is not None:
        print("Solution found e^-x / (e - 1):", solution)
    else:
        print("Solution not found within max iterations.")


if __name__ == "__main__":
    main()