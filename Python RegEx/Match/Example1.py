#Do a search taht will return a match object:

import re

txt = "The rain in spain"
x = re.search("ai", txt)
print(x) #this will print an object