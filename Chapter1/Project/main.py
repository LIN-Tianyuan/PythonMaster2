from file_define import TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JsonFileReader("February2023SalesData.txt")

january_data:list = text_file_reader.read_data()
february_data:list = json_file_reader.read_data()
all_data:list = january_data + february_data

# {"2013-01-01": 1234, "2023-01-02": }
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += int(record.money)
    else:
        data_dict[record.date] = int(record.money)

bar = Bar(init_opts=InitOpts(theme=ThemeType.WHITE))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('Sales', list(data_dict.values()))
label_ops = LabelOpts(is_show=False)
bar.set_global_opts(
    title_opts=TitleOpts(title="Daily Sales")
)

bar.render('Daily sales bar chart.html')

