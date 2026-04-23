PATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\even_odd_separator\\"
numbers = []
even = []
odd = []
with open(PATH + "numbers", "r") as file:
    for line in file:
        numbers.append(line)
