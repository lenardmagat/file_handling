import json
import logging
logging.basicConfig(level=logging.INFO)


class Student_class:
    def __init__(self):
        self.FILEPATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\identifying_highest_gwa\\class.json"

    def get_students_data(self):
        try:
            with open(self.FILEPATH, 'r') as file:
                data = json.load(file)
            logging.info("Successfully read the file")
            return data.get("students")
        except Exception as e:
            logging.warning(e)

    def get_highest_gwa(self):
        gwa = []
        data = self.get_students_data()
        for i in data:
            gwa.append(i.get("gwa"))
        logging.info("successfully obtain student's GWA")
        highest_grade = gwa.index(min(gwa))
        logging.info("successfully obtain student data who has highest GWA")
        print(f"{data[highest_grade].get('name')} got {data[highest_grade].get('gwa')} which is the highest in the class")

if __name__ == "__main__":
    Student_class().get_highest_gwa()