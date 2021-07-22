import random
import string

# extracting ascii 
lower= string.ascii_lowercase
upper =string.ascii_uppercase
nun =string.digits
symbol=string.punctuation

# randomising each extract
lo =random.sample(lower,2)
up =random.sample(upper,2)
nu =random.sample(nun,2)
sy =random.sample(symbol,2)

# concatenating extractions
all = lo + up + nu + sy

# joing and removing spacing
passcode = ''.join(all)

# outputing the passcode
print('Generated passcode is: '+passcode)