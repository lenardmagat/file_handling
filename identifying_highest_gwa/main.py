import json
import logging
logging.basicConfig(level=logging.INFO)
PATH = "C:\\Users\\Marry Bless Magat\\Documents\\Lenard Files\\arduino ide\\file_handling\\identifying_highest_gwa\\class.json"
gwa = []
try:
    with open(PATH, 'r') as file:
        data = json.load(file)
    logging.info("Successfully read the file")
except Exception as e:
    logging.warning(e)

data_value = data.get("students")
for i in data_value:
    gwa.append(i.get("gwa"))
logging.info("successfully obtain student's GWA")
highest_grade = gwa.index(min(gwa))
logging.info("successfully obtain student data who has highest GWA")
print(f"{data_value[highest_grade].get('name')} got {data_value[highest_grade].get('gwa')} which is the highest in the class")
