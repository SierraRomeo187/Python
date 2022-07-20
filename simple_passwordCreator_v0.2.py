import string
from random import *
chars_sym_numb = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(chars_sym_numb) for x in range(randint(8, 16)))
print ("This is your random generated password =" , password)