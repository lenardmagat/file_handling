import logging
PATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\multiple_line_saving\\mylife.txt"
more_line = True
def saving_user_input(data : str):
    with open(PATH, "a") as file:
        file.write("\n" + data)

while more_line:
    data = input("Enter line")
    saving_user_input(data)
    while True:
        check_status = input("Are there more lines y/n: ").strip().lower()
        if check_status == "y":
            break
        elif check_status == "n":
            more_line = False
            break
        continue