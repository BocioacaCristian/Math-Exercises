#- Find the sum of the squares of the first n natural numbers
import math
def sum_Of_Squares(n):
    list_of_numbers = list(range(0,n+1))
    list_of_squares = []
    sum_of_numbers = 0
    for i in list_of_numbers:
        if (math.sqrt(i)).is_integer():  # math.sqrt(i) Calculates the root of the number "i" and is_integer checks if it is a whole number.
            list_of_squares.append(i)
    print(list_of_squares)

    for num in list_of_squares:
        sum_of_numbers += num

    return f"The sum of the squares is {sum_of_numbers}"

