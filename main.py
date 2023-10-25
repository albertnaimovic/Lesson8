# 1. Create a variables containing strings for username and password. Start Endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print greeting message.

# credentials_dict = {'albis': 'xa22*', 'jonas': 'ada94-', 'giedrius': 'aaa', 'tadas': 'tadasxx1', 'mariux': 'mariux'}
# wrong_credentials_counter = 0

# while True:
#     input_username = input("Enter your username: ")
#     input_password = input("Enter your password: ")

#     if input_username in credentials_dict:
#         if input_password == credentials_dict[input_username]:
#             print("You have logged in successfully")
#             break
#         else:
#             wrong_credentials_counter += 1
#             print(f"Wrong password, it was your {wrong_credentials_counter} attempt.")
#     else:
#         wrong_credentials_counter += 1
#         print(f"Wrong credentials, it was your {wrong_credentials_counter} attempt.")


# 2. Allow user to enter 10 integers, and then print the sum and average of those entered numbers.

# my_list = []

# for i in range(10):
#     my_list.append(int(input(f"Enter num {i+1}: ")))

# print(f"Sum: {sum(my_list)}\nAVG: {sum(my_list)/10}")


# 3. Generate a dictionary of 10 keys being 1,2,3...10 each of them should store a value of random integer number from 1 to 100.

# import random
# my_dict = {}

# for i in range(10):
#     temp_dict = {i+1: random.randint(1, 100)}
#     my_dict.update(temp_dict)
# print(my_dict)

# 4. Create a pin code cracker. Let's say pin code consists of 4 random digits. You can store the value in variable.
#  Then create a loop going through all possible combinations until you find the one you entered.

# import random

# pincode = random.randint(1000, 9999)
# print(pincode)
# cracker = 1000

# while cracker != pincode:
#     cracker += 1
# print(f"Pincode cracked: {cracker}")

#Task number 4

import time

pin = '0000'
locked = True

start_time = time.perf_counter()
while locked:
    for digit1 in range(10):
        for digit2 in range(10):
            for digit3 in range(10):
                for digit4 in range(10):
                    current_attempt = f"{digit1}{digit2}{digit3}{digit4}"
                    if current_attempt == pin:
                        print(f"Pin Cracked! The correct pin is: {current_attempt}")
                        locked = False

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time} seconds')

# eggs = 10
# def cooking_time(eggs):
#     if eggs == 0:
#         return 0
#     elif eggs % 8 == 0:
#         return ((eggs // 8)) * 5
#     elif eggs % 8 != 0:
#         return ((eggs // 8)+1) * 5
        

# a = 456
# b = 1734
# result = 1180
# a_list = list(map(int, str(a)))
# b_list = list(map(int, str(b)))

# all_users = {"aaa": "111", "bbb": "222", "ccc": "333"}
# while True:
#     entered_username = input("Enter your username: ")
#     entered_password = input("Enter your password: ")
#     # if username in all_users and all_users[username] == password: # si eilute is GPTchat
#     for username, password in all_users.items():
#         if entered_username == username and entered_password == password:
#             print("welcome")
#             break
#     else:
#         print("Wrong")
#         continue
#     break