# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check ff credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials' and ask to enter password and username again.
# The program should show numbers of times you tried to enter both credentials.
# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, names 'improved password'

# credentials_database = input("Enter username and password database: ")
# credentials_database = "username='albis', password='xa22*'; username='jonas',password='ada94-'; username='giedrius', password='aaa'; username='tadas', password='tadasxx1';"
credentials_database = "username='Albis', password='xa22*'; username='Jonas', password='ada94-'; username='giedrius', password='aaa'; username='tadas', password='tadasxx1'; username='mariux', password='mariux';"

if credentials_database[-1] == ";":
    credentials_database = credentials_database[:-1]

credentials_database = credentials_database.replace(" ", "")
list_of_credentials = credentials_database.lower().split(";")
word_counter = len(list_of_credentials)

if word_counter < 5:
    while word_counter < 5:
        print("You've entered less than five credentials.")
        credentials_database = input("Enter username and password database: ")
        if credentials_database[-1] == ";":
            credentials_database = credentials_database[:-1]
        credentials_database = credentials_database.replace(" ", "")
        list_of_credentials = credentials_database.lower().split(";")
        word_counter = len(list_of_credentials)


credentials_dict = {}

for item in list_of_credentials:
    cleaned_string = item.replace("username='", "").replace("',password='", ",").replace("'", "")
    pair_list = cleaned_string.split(',')
    temp_dict = {pair_list[0]: pair_list[1]}
    credentials_dict.update(temp_dict)

print(credentials_dict)

while_value = False
wrong_credentials_counter = 0

while while_value == False:
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    if input_username in credentials_dict:
        if input_password == credentials_dict[input_username]:
            while_value = True
            print("You have logged in successfully")
            break
        else:
            wrong_credentials_counter += 1
            print(f"Wrong password, it was your {wrong_credentials_counter} attempt.")
    else:
        wrong_credentials_counter += 1
        print(f"Wrong credentials, it was your {wrong_credentials_counter} attempt.")

