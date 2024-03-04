FILE_NAME_Q1 = "name.txt"
FILE_NAME_Q3 = "numbers.txt"

# Question 1
print("Python File Question 1")
user_name = input("Name: ")
out_file = open(FILE_NAME_Q1, "w")
print(user_name, file=out_file)
out_file.close()
print()

# Question 2
print("Python File Question 2")
in_file = open(FILE_NAME_Q1, "r")
name = in_file.read().strip()
print(f"Your name is {name}.")
in_file.close()
print()

# Question 3
print("Python File Question 3")
in_file = open(FILE_NAME_Q3, "r")
first_number = int(in_file.readline().strip())
second_number = int(in_file.readline().strip())
total = first_number + second_number
print(f"The total of first two numbers is {total}.")
in_file.close()
print()

# Question 4
print("Python File Question 4")
in_file = open(FILE_NAME_Q3, "r")
total = 0
for line in in_file:
    total += int(line)
print(f"The total numbers is {total}.")
in_file.close()
print()
