# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# # data_dict = data.to_dict()
# # print(data_dict["temp"])
# #
# # temp_serie_to_list = data["temp"].to_list()
# #
# # print(data["temp"].max())
# #
# # print(data["condition"])
# # print(data.condition)
#
# #Data in a row
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)
#
# #Create data frame from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data =pandas.DataFrame(data_dict)
# print(data)

# data.to_csv("new_data.csv")

data = pandas.read_csv("squirrel_data.csv")
squirrel_colors = data["Primary Fur Color"].dropna()
squirrel_colors_dict = {"color": [], "count": []}
squirrel_colors_dict_temp = {}


for row in squirrel_colors:
    if row not in squirrel_colors_dict_temp:
        squirrel_colors_dict_temp[row] = 0
    squirrel_colors_dict_temp[row] += 1

print(squirrel_colors_dict_temp)

for key in squirrel_colors_dict_temp:
    if key not in squirrel_colors_dict:
        if key == "Cinnamon":
            squirrel_colors_dict["color"].append("Red")
            squirrel_colors_dict["count"].append(squirrel_colors_dict_temp[key])
        else:
            squirrel_colors_dict["color"].append(key)
            squirrel_colors_dict["count"].append(squirrel_colors_dict_temp[key])

print(squirrel_colors_dict)

squirrel_colors_converted = pandas.DataFrame(squirrel_colors_dict)
squirrel_colors_converted.to_csv("squirrel_colors.csv")