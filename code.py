# quadratic_root_calculator
# by brussels-sprout


def title():
    print("\033[1m" + "Real root calculator for quadratic functions" +
          "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


def input_():
    print("For f(x) = ax² + bx + c, where a ≠ 0, input:")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    dp = input("Number of decimal places to give result to: ")
    return a, b, c, dp


def check_digit(i, j, z, w):  # checks if i, j, z, and w are digits
    to_check = [i, j, z, w]
    checked = []
    for element in to_check:
        element_bool = element.lstrip("-").replace(".", "", 1).isdigit()
        checked.append(element_bool)
    return checked


# checks if i (string digit or float or integer) is not equal to zero
def check_nonzero(i):
    return float(i) != 0


# checks if i (string digit or float or integer) is a positive integer
def check_positive_int(i):
    if i == float("inf"):
        return True
    else:
        return i > 0 and i.is_integer()


# turns  i, j, and z (strings) into floats
def str_to_float(i, j, z, w):
    return float(i), float(j), float(z), float(w)


# turns i (digit) to an integer
def digit_to_int(i):
    return int(i)


# processes determinant (i), b (j), and a (z) of a f(x)
# and returns result with a certain number of decimal places (w)
def operation(i, j, z, w):
    if i > 0:
        x1 = (-j + i ** (1 / 2)) / 2 * z
        x2 = (-j - i ** (1 / 2)) / 2 * z
        print(f"For f(x) = 0, x = {round(x1, w)} or x = {round(x2, w)}.")
    elif i == 0:
        x = -j / (2 * z)
        print(f"For f(x) = 0, x = {round(x, w)} (double root).")
    else:
        print("For f(x) = 0, x ∉ ℝ.")


# calculates the determinant of a f(x) = ax² + bx + c, where
# a is i, b is j, and c is z
def determinant(i, j, z):
    return j ** 2 - 4 * i * z


def end():
    ask = input("\nInput any character(s) to make a new calculation or simply "
                "press ENTER to exit: ")
    if ask == "":
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
                    raise ValueError
            else:
                print("Please input a ≠ 0.")
                main()
        else:
            raise ValueError
    except (OverflowError, MemoryError):
        print("Number(s) too large.")
        main()
    except ValueError:
        print("Please input a positive integer for the number of "
              "decimal places.\n")
        main()


title()
main()
