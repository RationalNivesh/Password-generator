
import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijkmnopqrstuvwxyz"
symbols="~!@#$%^&*()_+"
numbers="0123456789"
len=10
all=upper+lower+symbols+numbers
passcode="".join(random.sample(all,len))
print("Your password is:", passcode)
