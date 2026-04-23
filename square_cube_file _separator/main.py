import logging
logging.basicConfig(level=logging.INFO)
PATH = "square_cube_file _separator\\"


class interger_separator:
    def __init__(self):
        self.FILE_PATH = PATH
    def saving_file(self, file_name : str, data : list):
        try:
            with open(self.FILE_PATH + file_name, "w") as file:
                file.write(",".join(str(i) for i in data))
            logging.info(f"successfully save the data in {file_name}")
        except Exception as e:
            logging.warning(e)

    def main(self, data : list):
        squared_even = []
        cube_odd = []
        for i in data:
            if i % 2 == 0:
                squared_even.append(i * i)
                continue
            cube_odd.append(i * i * i)
        self.saving_file("double.txt", squared_even)
        self.saving_file("triple.txt", cube_odd)
        logging.info("Exiting the system")

try:
    with open(PATH + "numbers.txt", "r") as file:
        data = file.read()
        numbers = list(map(int, data.split(",")))
    logging.info(f"success reading the numbers.txt file")
except Exception as e:
    logging.warning(e)

interger_separator().main(numbers)