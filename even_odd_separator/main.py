import logging
logging.basicConfig(level=logging.INFO)
PATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\even_odd_separator\\"
numbers = []
even = []
odd = []

def create_file(file_name, data):
    try:
        with open(PATH + file_name, "w") as file:
            file.write(" ".join(str(i) for i in data))
        logging.info("Successfully created a file")
    except Exception as e:
        logging.warning(e)

with open(PATH + "numbers.txt", "r") as file:
    try:
        for line in file:
            numbers.append(float(line.strip()))
        logging.info("Success reading the file")
    except Exception as e:
        logging.warning(e)

for i in numbers:
    if i % 2 == 0:
        even.append(i)
        continue
    odd.append(i)

create_file("even_numbers.txt", even)
create_file("odd_numbers.txt", odd)
