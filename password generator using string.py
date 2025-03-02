

import string
import random
if __name__ == "__main__":

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    length = int(input("Enter the password length that you wants\n "))

    s = []

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)

    print("".join(s[0:length]))
