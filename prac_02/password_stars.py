MIN_LEN = 6


def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print("PW: ", end='')
    for i in range(len(password)):
        print("*", end='')
    print()


def get_password():
    password = input(f"PW(minimum length:{MIN_LEN}): ")
    while len(password) < MIN_LEN:
        print("Invalid Password")
        password = input(f"PW(minimum length:{MIN_LEN}): ")
    return password


main()
