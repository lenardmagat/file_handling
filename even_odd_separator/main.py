PATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\even_odd_separator\\"
numbers = []
even = []
odd = []
with open(PATH + "numbers.txt", "r") as file:
    for line in file:
        numbers.append(float(line.strip()))

for i in numbers:
    if i % 2 == 0:
        even.append(i)
        continue
    odd.append(i)
