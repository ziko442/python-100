# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#
# print(temp)

import pandas as pd

file_path = "weather_data.csv"

data = pd.read_csv(file_path)
# print(data["temp"].to_list())
# print(data["temp"].mean())
# print(data["temp"].max())

var = data[data["temp"] == data["temp"].max()]
print(var)

