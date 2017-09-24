import re

num_lines = sum(1 for line in open("Kaartnummers.txt"))
print("Deze file telt", num_lines, "regels")

int = open("Kaartnummers.txt", "r")

file = open("Kaartnummers.txt", "r")

file = file.read()

numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)

num_max = max(numbers)
print("Het grootste kaartnummer is:", num_max,"en dat staat op regel", numbers.index(num_max)+1)

'''de +1 is omdat de index telt vanaf 0 en de opdracht dit niet moet.
Ik zou het anders niet weten.'''