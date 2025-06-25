from file_define import TextFileReader, JsonFileReader

text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JsonFileReader("February2023SalesData.txt")

january_data:list = text_file_reader.read_data()
february_data:list = json_file_reader.read_data()
all_data:list = january_data + february_data



