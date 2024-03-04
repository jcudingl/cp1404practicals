"""
CP1404/CP5632 - Practical
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            status = determine_status(score)
            print(status)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print()
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def show_stars(score):
    for i in range(len(score)):
        print("*", end='')
    print()


def get_valid_score():
    score = input("Enter score: ")
    while float(score) < 0 or float(score) > 100:
        print("Invalid score")
        score = input("Enter score: ")
    return score


def determine_status(score):
    if float(score) >= 90:
        return "Excellent"
    if float(score) >= 50:
        return "Passable"
    return "Bad"


main()
