# quadratic_root_calculator
# by brussels-sprout


def title():
    print("\033[1m" + "Real root calculator for quadratic functions" + "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


def input_():  # get input of four numbers
    print("For f(x) = ax² + bx + c, where a ≠ 0, input:")
    return input("a = "), input("b = "), input("c = "), input("Number of decimal places to give result to: ")


def check_digit(i, j, z, w):  # checks if i, j, z, and w are digits
    return i.lstrip("-").replace(".", "", 1).isdigit() and j.lstrip("-").replace(".", "", 1).isdigit() and \
           z.lstrip("-").replace(".", "", 1).isdigit() and w.lstrip("-").replace(".", "", 1).isdigit()


def check_nonzero(i):  # checks if i (string digit or float or integer) is not equal to zero
    return float(i) != 0


def check_positive_int(i):  # checks if i (string digit or float or integer) is a positive integer
    if i == float("inf"):
        return True
    else:
        return i > 0 and i.is_integer()


def str_to_float(i, j, z, w):  # turns  i, j, and z (strings) into floats
    return float(i), float(j), float(z), float(w)


def digit_to_int(i):  # turns i (digit) to an integer
    return int(i)


def operation(i, j, z, w):  # processes determinant (i), b (j), and a (z) of a f(x)  and returns result with a certain number
    # of decimal places (w)
    if i > 0:
        x1 = (-j + i ** (1 / 2)) / 2 * z
        x2 = (-j - i ** (1 / 2)) / 2 * z
        print(f"For f(x) = 0, x = {round(x1, w)} or x = {round(x2, w)}.")
    elif i == 0:
        x = -j / (2 * z)
        print(f"For f(x) = 0, x = {round(x, w)} (double root).")
    else:
        print("For f(x) = 0, x ∉ ℝ.")


def determinant(i, j, z):  # calculates the determinant of a f(x) = ax² + bx + c, where a is i, b is j, and c is z
    return j ** 2 - 4 * i * z


def end():
    if input("\nInput any character(s) to make a new calculation or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        main()


def main():
    try:
        a, b, c, dp = input_()
        if check_digit(a, b, c, dp):
            a, b, c, dp = str_to_float(a, b, c, dp)
            if check_nonzero(a):
                if check_positive_int(dp):
                    operation(determinant(a, b, c), b, a, digit_to_int(dp))
                    end()
                else:
                    print("Please input a positive integer for the number of decimal places.")
                    main()
            else:
                print("Please input a ≠ 0.")
                main()
        else:
            print("Please input a ∈ ℝ, b ∈ ℝ, and c ∈ ℝ without illegal characters.")
            main()
    except (OverflowError, MemoryError):
        print("Number(s) too large.")
        main()


title()
main()
