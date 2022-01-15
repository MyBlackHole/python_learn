import os
import re

# for i in os.listdir("."):
#     if (os.path.isdir(i)):
#         name = re.findall("\d+_(.*)", i)
#         for j in os.listdir(i):
#             old = i + '/' + j
#             new = i + '/' + name[0] + '.md'
#             print(old)
#             print(new)
#             os.renames(old, new)


with open('./param_1243.js', 'r') as f:
    text = f.read()

print(text)
