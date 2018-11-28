"""
-Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

-add movies
-see movies
-find a movie
-stop running the program

Tasks:
[]: Decide where to stor movies
[]: what is the format of the movie?
[]: show the user the main interface and get their input
[]: allow users to add movies
[]: show all their movies
[]: find a movie
[]: stop running the program when they type 'q'

"""


def add_m():
    print("add")


def show_m():
    print("view")


def find_m():
    print("find")


def menu():
    user_input = input("Enter 'a' = add, 'l' = view all, 'f' = find, 'q' = quit:")

    while user_input != 'q':

        if user_input == 'a':
            add_m()

        elif user_input == 'l':
            show_m()

        elif user_input == 'f':
            find_m()

        else:
            print("Unknown command - please try again.")

        user_input = input("Enter 'a' = add, 'l' = view all, 'f' = find, 'q' = quit:")

    else:
        print("stopping program.....")


menu()

