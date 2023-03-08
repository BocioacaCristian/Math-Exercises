#- Find the sum of the squares of the first n natural numbers
import math
def sum_Of_Squares(n):
    list_of_numbers = list(range(0,n+1))
    list_of_squares = []
    sum_of_numbers = 0
    for i in list_of_numbers:
        if (math.sqrt(i)).is_integer():  # math.sqrt(i) Calculates the root of the number "i" and is_integer checks if it is a whole number.
            list_of_squares.append(i)

    for num in list_of_squares:
        sum_of_numbers += num

    return sum_of_numbers

def test_sum():
    #Let's test the sum first.
    passed = True
    try:
        assert sum_Of_Squares(10) == 14
        print("Test 1 Passed!")
    except AssertionError:
        print("Test 1 failed! Check if the result is correct or if the input is an integer!")
        passed = False

    #Let's test if we put a string instead of an integer

    try:
        assert sum_Of_Squares("10") == 14
        print("Test 2 Passed!")
    except TypeError:
        print("Test 2 failed! Check if the result is correct or if the input is an integer!")
        passed = False

    #Let's test if we put a wrong result

    try:
        assert sum_Of_Squares(10) == 10
        print("Test 3 Passed!")
    except AssertionError:
        print("Test 3 failed! Check if the result is correct or if the input is an integer!")
        passed = False

    if passed:
        print("All the test have passed")
    else:
        print("Some of the tests failed. Go check what happened.")

test_sum()