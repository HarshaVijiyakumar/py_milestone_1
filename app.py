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

{     'name': 'The Matrix',     'director': 'Wachowskis',     'year': '1994' }


"""


list_of_mov = [{
        'name': 'mov1',
        'director': 'dir1',
        'year': 1994
        },
        {
        'name': 'mov2',
        'director': 'dir1',
        'year': 1995
        },
        {
        'name': 'mov3',
        'director': 'dir1',
        'year': 1996
        },
        {
        'name': 'mov3',
        'director': 'dir2',
        'year': 2000
        }]


def add_m():
    mov_name = input("enter a name:")
    dir_name = input("enter a dir name:")
    when_mov_came = int(input("year of mov (yyyy):"))
    list_of_mov.append({'name': mov_name, 'director': dir_name, 'year': when_mov_came})
    print(f"your {mov_name} movie successfully added")


def show_m():
    print(list_of_mov)


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

