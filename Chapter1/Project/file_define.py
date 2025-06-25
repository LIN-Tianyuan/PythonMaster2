from data_define import Record
import json

class FileReader:
    def read_data(self):
        pass

class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self):
        f = open(self.path, "r", encoding='UTF-8')
        # print(f.readlines())
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            date = data_list[0]
            order_id = data_list[1]
            money = data_list[2]
            province = data_list[3]

            record = Record(date, order_id, money, province)
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self):
        f = open(self.path, "r", encoding='UTF-8')

        record_list: list[Record] = []
        for line in f.readlines():
            data_rect = json.loads(line)
            date = data_rect["date"]
            order_id = data_rect["order_id"]
            money = data_rect["money"]
            province = data_rect["province"]
            record = Record(date, order_id, money, province)
            record_list.append(record)

        f.close()
        return record_list
if __name__ == '__main__':
    """
    text_file_reader = TextFileReader("January2023SalesData.txt")
    r_list = text_file_reader.read_data()
    for record in r_list:
        print(record)
    """
    json_file_reader = JsonFileReader("February2023SalesData.txt")
    r2_list = json_file_reader.read_data()
    for record in r2_list:
        print(record)

