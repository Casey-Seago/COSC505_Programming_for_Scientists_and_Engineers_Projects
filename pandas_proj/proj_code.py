#  loading necessary packages
import pandas as pd
import matplotlib.pyplot as plt

#  importing dataset as a csv and printing columns

data = pd.read_csv("http://web.eecs.utk.edu/~smarz1/courses/cosc505/moderna.csv")
print(data.columns)

#  looking at data regions by printing the second column
print(data.iloc[:, 1])

# printing the first column
print(data.iloc[:, 0])

# creating a list of weeks that vaccines were allocated called weeks
data = pd.read_csv("https://data.cdc.gov/api/views/b7pe-5nws/rows.csv?accessType=DOWNLOAD")
week = data["Week of Allocations"]
weeks = week.drop_duplicates()
print(weeks)

# convert weeks from a series to a list
weeks = weeks.tolist()

# creating a dataframe that totals the number of 1st and 2nd doses based on date
grouped = data.groupby([data.iloc[:,1]]).sum()


# creating lists of the values from the first and second dose columns
first = grouped['1st Dose Allocations'].tolist()
second = grouped['2nd Dose Allocations'].tolist()

# data in weeks is in the wrong order (april 2021 dates come before december 2020 dates) so I am flipping it
weeks_empty = []
for i in range(len(weeks)-1, -1, -1):
    weeks_empty.append(weeks[i])
weeks = weeks_empty.copy()

# data in first and second is also out of order, so I am putting the december dates at the start
my_order = [15, 16, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] # needs to be in this order
first = [first[i] for i in my_order]
second = [second[i] for i in my_order]

####### plot is two lines, one for each dose, on one plot: #######
plt.figure(2)
# plotting line 1 points
plt.plot(weeks, first, label = "1st Dose Allocations", color="green", linestyle = "dashed", marker = "o", markerfacecolor = "green")

# plotting line 2 points
plt.plot(weeks, second, label = "2nd Dose Allocations", marker = "o")

# naming the axes and title
plt.xlabel("Week of Allocations")
plt.ylabel("Total Doses Allocated")
plt.title("Total Doses Allocated per Week")
plt.xticks(rotation = 45)
plt.legend()
plt.tight_layout()
plt.savefig('dose_allocations.png')
