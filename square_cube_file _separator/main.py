import logging
logging.basicConfig(level=logging.INFO)
PATH = "square_cube_file _separator\\"
numbers = []
even = []
odd = []
try:
    with open(PATH + "numbers.txt", "r") as file:
        data = file.read()
        numbers = list(map(int, data.split(",")))
except Exception as e:
    pass
