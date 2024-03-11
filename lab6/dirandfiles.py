
import os
from colorama import Fore, init

init(autoreset=True)
path = input("Input a path: ")
for dirpath, dirnames, filenames in os.walk(path, '.'):
    print(Fore.BLUE + str(dirpath))
    for f in filenames:
        print(os.path.join(dirpath, f))
    print("\n")




path1 = input("Input a path: ")

print(f"{path1} exists: {os.access(path1, os.F_OK)}")
print(f"{path1} is readable: {os.access(path1, os.R_OK)}")
print(f"{path1} is writeable: {os.access(path1, os.W_OK)}")
print(f"{path1} is executable: {os.access(path1, os.X_OK)}")



path1 = input("Input a path: ")

if os.access(path1, os.F_OK):
    print(f"The path {path1} exists!")
    if os.path.isfile(path1):
        print(f"The directory portion of the path: {os.path.dirname(path1)}")
        print(f"The filename portion of the path: {os.path.basename(path1)}")
    else:
        print(f"The directory of the path: {path1}")
else:
    print(f"The path {path1} does not exist")



f = open("text4.txt", "r")
print(len(f.readlines()))
f.close()



f = open("text5.txt", "w")
li = input("Input a list of values separated by commas: ").split(", ")
f.write(str(li))
f.close()


from string import ascii_uppercase

new_path = "labs\\lab6\\alphabet"
if not os.access(new_path, os.F_OK):
    os.makedirs(new_path)

for letter in ascii_uppercase:
    f = open(f"{new_path}\\{letter}.txt", "w")
    f.write(f"This is {letter}'s txt file")
    f.close()



with open("builtin_func.txt", "r") as f1:
    f2 = open(f"copy_builtin_func.txt", "w")
    for line in f1:
        f2.write(line)
    f1.close()



path = input()

if os.access(path, os.F_OK):
    print(f"File is readeable: {os.access(path, os.R_OK)}\nFile is writeable: {os.access(path, os.W_OK)}")
    os.remove(path)
    print("The file is Deleted")

