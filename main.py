import string
import random

if __name__ == "__main__":
    string_lc = string.ascii_lowercase
    string_uc = string.ascii_uppercase
    string_dig = string.digits
    string_pun = string.punctuation

    while True:
        user_in = input("Enter Password length: ")
        isPWLenNum = user_in.isdigit()

        if isPWLenNum == True:
            pw_len = int(user_in)

            string_combined = []
            string_combined.extend(string_lc)
            string_combined.extend(string_uc)
            string_combined.extend(string_dig)
            string_combined.extend(string_pun)

            print("Your random password: ")
            print("".join(random.sample(string_combined, pw_len)))
            break
        else:
            print("Please enter integer")