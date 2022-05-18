# CSV - Comma Separated Values

# TODO 1: Open weather_data.csv & create a list named data that contains the values from the file.

# with open("weather_data.csv") as report:
#     data = report.readlines()
#     print(data)
# This would take a lot of "cleaning" in order to use each of columns.

# # This is an inbuilt library for tabular data (i.e. data displayed in columns/tables)
# import csv
# with open("weather_data.csv") as report:
#     data = csv.reader(report) # Read cvs file by its rows
#     temps = []
#     for row in data:  # Separates the temp column data
#         print(row)
#         if row[1] != "temp":  # != "temp" because a char cannot be an int.
#             temps.append(int(row[1]))
# print(temps)

# TODO 2: Practice using pandas.
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])  # Prints "temp" series (i.e. column) from CVS file

dict_data = data.to_dict()  # Coverts DATAFRAME into a dictionary
day_list = data["day"].to_list()  # Coverts "day" series into a list
temp_list = data["temp"].to_list()  # Coverts "temp" series into a list

print(dict_data)
print(day_list)
print(temp_list)

# TODO 3: Calculate the average(i.e.mean) of "temp" column.
# Calculated average using operators
num_1 = temp_list[0]
temp_count = len(temp_list)
for temp in temp_list[1:]:
    num_1 += temp
# temp_sum = sum(temp_list) #Another way to calculate sum of all temp
avg_temp = num_1 / temp_count
print(f"The average temperature is: {avg_temp} ")

# Calculated average using pandas Series method
average_temp = data["temp"].mean()
print(average_temp)

# TODO 3: Find the highest value in "temp" column.
max_temp = data["temp"].max()
print(max_temp)

# NOTES:
# pandas takes the first row as the names of the columns, so it can find correspoding data when the names are called
# 2 Main data types in pandas:
#  DATA FRAME is your whole table
# SERIES is the columns (i.e. list)


# When retrieving data from a column pandas actually taken and converted the heading into attributes
# Just ensure it has the same capitalization as how it is written in the CSV file
# As a result and alternative way is:

# TODO 3.1: Get data from columns
max_temp2 = data.temp.max()
print(max_temp2)

# TODO 4: Get data from row.
monday = data[data.day == "Monday"]
print(monday)  # Searches the "days" column for "Monday", a retrieves its row

# TODO 4.1: Get the row for the day that had the highest temp.
print(data[data.temp == max_temp2])

# You can also use the retrieved data with the headings
m_temp = int(monday.temp)
m_cond = monday.condition

print(f"The forecast for Monday will be {m_cond}, and have a high of {m_temp} degrees.")

# TODO 5: Convert Monday's temp from degrees to ferenhiet
m_f_temp = m_temp * 9/5 + 32
print(f"Monday's temperature in degrees is {m_f_temp}")



# TODO 6: Create a dataframe from scratch usign data inside python (i.e not from an outside file).
grade_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
grade_data = pandas.DataFrame(grade_dict)
grade_data.to_csv("grade_data.csv")
print(f"\n{grade_data}")