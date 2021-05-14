# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# native way to get data using csv module
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# using pandas module to easily get data
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))  # data["temp"] same as data.temp

data_dict = data.to_dict()  # change to dict type
print(data_dict)

temp_list = data["temp"].to_list()  # change to list type
print(temp_list)
# Calculate average temperature from the list(native way)
print(sum(temp_list) / len(temp_list))
# Calculate average temperature from the list(pandas way)
print(data["temp"].mean())
# Get max temperature from the list
print(data["temp"].max())

row = data[data.day == "Monday"]  # get the row data for Monday
print(row)

max_temp_day = data[data.temp == data.temp.max()]  # get the day that has the max temperature
print(max_temp_day.day)

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(monday_temp * 9/5 + 32)  # convert to fahrenheit

# Create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")  # convert to csv and save to file with name specified
