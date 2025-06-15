from data_define import Record

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
    pass
if __name__ == '__main__':
    text_file_reader = TextFileReader("January2023SalesData.txt")
    r_list = text_file_reader.read_data()
    for record in r_list:
        print(record)
