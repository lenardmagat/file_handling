import logging
logging.basicConfig(level=logging.INFO)
class Even_odd_separator:
    def __init__(self):
        self.FILE_PATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\even_odd_separator\\"
        self.even = []
        self.odd = []
    def create_file(self, file_name, data):
        try:
            with open(self.FILE_PATH + file_name, "w") as file:
                file.write(" ".join(str(i) for i in data))
            logging.info("Successfully created a file")
        except Exception as e:
            logging.warning(e)
    def get_data(self):
        numbers = []
        with open(self.FILE_PATH + "numbers.txt", "r") as file:
            try:
                for line in file:
                    numbers.append(float(line.strip()))
                logging.info("Success reading the file")
                return numbers
            except Exception as e:
                logging.warning(e)

    def serate_even_and_odd_integer_and_save(self):
        numbers = self.get_data()
        for i in numbers:
            if i % 2 == 0:
                self.even.append(i)
                continue
            self.odd.append(i)

        self.create_file("even_numbers.txt", self.even)
        self.create_file("odd_numbers.txt", self.odd)

if __name__ == "__main__":
    Even_odd_separator().serate_even_and_odd_integer_and_save()
