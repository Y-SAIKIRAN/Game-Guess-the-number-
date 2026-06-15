import random
import string

pass_len=10
charValue = string.ascii_letters + string.punctuation + string.digits

# password=""
# for i in range(pass_len):
#     password+=random.choice(charValue)
# print("Your random password is: ",password)

password= "".join([random.choice(charValue) for i in range(pass_len)])
print(password)