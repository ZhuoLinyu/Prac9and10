def do_it(n):

    if n <= 0:

        return 0

    return n % 2 + do_it(n - 1)



def do_something(n):

    if n < 0:

        return

    print(n ** 2)

    do_something(n - 1)


do_something(4)

def calculate_blocks(rows):

    if rows <= 0:

        return 0

    return rows + calculate_blocks(rows - 1)





def build_pyramid():

    chosen_rows = int(input("How many rows is your pyramid: "))

    print("For {} rows, you need {} blocks".format(chosen_rows,

                                                   calculate_blocks(

                                                       chosen_rows)))