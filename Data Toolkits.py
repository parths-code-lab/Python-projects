def get_numbers():
    user_value = input("Enter the numbers to perform operation on : ")
    values_str = user_value.split()
    values_int = []

    for i in values_str:
        try:
            values_int.append(int(i))
        except ValueError:
            print("Invalid Input :", i)

    return values_int


def sort_numbers(values_int):
    values_sort = sorted(values_int)
    print("Sorted List :", values_sort)
    print()


def find_max_min(values_int):
    values_max = max(values_int)
    values_min = min(values_int)
    print("Maximum value :", values_max)
    print("Minimum value :", values_min)
    print()


def remove_duplicates(values_int):
    values_no_duplicate_set = set(values_int)
    values_no_duplicate_list = list(values_no_duplicate_set)

    if len(values_int) == len(values_no_duplicate_set):
        print("No duplication found original list :", values_int)
    else:
        print("List without duplication :", values_no_duplicate_list)
    print()


def square_numbers(values_int):
    values_sqr = []
    for val in values_int:
        val_sqr = val * val
        values_sqr.append(val_sqr)

    print("Squared value of list :", values_sqr)
    print()


def filter_even(values_int):
    values_even = []
    for val in values_int:
        if val % 2 == 0:
            values_even.append(val)

    print("Even values of list :", values_even)
    print()


def menu():
    print("--- Smart Data Toolkit ---")
    print("1 Sort numbers")
    print("2 Find max/min")
    print("3 Remove duplicates")
    print("4 Square numbers")
    print("5 Filter even")
    print("6 Exit")


# program start directly
values_int = get_numbers()

while True:
    menu()

    try:
        user_input = int(input("Enter your choice : "))

        if not values_int:
            print("No operation can be performed on empty list")
            continue

        if user_input == 1:
            sort_numbers(values_int)

        elif user_input == 2:
            find_max_min(values_int)

        elif user_input == 3:
            remove_duplicates(values_int)

        elif user_input == 4:
            square_numbers(values_int)

        elif user_input == 5:
            filter_even(values_int)

        elif user_input == 6:
            print("Exiting Program...")
            break

        else:
            print("Invalid option please select again")

    except ValueError:
        print("Invalid Input")
