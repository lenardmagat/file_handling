import logging
logging.basicConfig(level=logging.INFO)
PATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\multiple_line_saving\\mylife.txt"
more_line = True
def saving_user_input(data : str):
    try:
        with open(PATH, "a") as file:
            file.write("\n" + data)
        logging.info(f"successfully save the user input: {data}")
    except Exception as e:
        logging.warning(e)

while more_line:
    data = input("Enter line: ")
    saving_user_input(data)
    while True:
        check_status = input("Are there more lines y/n: ").strip().lower()
        if check_status == "y":
            logging.info("user ask for another line")
            break
        elif check_status == "n":
            more_line = False
            logging.info("Ending the program!")
            break
        logging.warning("input y/n only!")
        continue