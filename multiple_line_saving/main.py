import logging
logging.basicConfig(level=logging.INFO)


class multi_line_saving:
    def __init__(self):
        self.FILE_PATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\multiple_line_saving\\mylife.txt"

    def saving_user_input(self, data : str):
        try:
            with open(self.FILE_PATH, "a") as file:
                file.write("\n" + data)
            logging.info(f"successfully save the user input: {data}")
        except Exception as e:
            logging.warning(e)

    def input_line_and_save(self):
        data = input("Enter line: ")
        self.saving_user_input(data)

    def check_status(self):
        while True:
            check_status = input("Are there more lines y/n: ").strip().lower()
            if check_status == "y":
                logging.info("user ask for another line")
                return True
            elif check_status == "n":
                more_line = False
                logging.info("Ending the program!")
                return False
            logging.warning("input y/n only!")
            continue
def main():
    while True:
        multi_line_saving().input_line_and_save()
        if multi_line_saving().check_status():
            continue
        break
    
if __name__ == "__main__":
    main()
   