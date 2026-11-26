
# learing to convert the data into visulization chart graph manula

import matplotlib.pyplot as plt 
# a simple matplotilb 
names = ["Amit", "Priya", "Rahul", "Sneha"]
marks = [85, 92, 45, 88]
age = [25, 15, 45, 65]
plt.bar(names, marks)

plt.title("Student Marks")
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.show()


# importing from the data csv file  pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataStudent .csv")
# it's a simple bar chart 
print(df.head())
print(df.columns)
plt.bar(df["Name"] , df["Marks"])
plt.title("Student Performance Analysis")
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.savefig("student_marks_chart.png")
plt.show()

dep_ana = df.groupby("Department")["Marks"].mean()
plt.bar(dep_ana.index, dep_ana.values)
plt.title("Department ana")
plt.xlabel("Department")
plt.ylabel("Mark")
plt.show()

#its line graphy also know as scatter plot
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
attendance = [80, 85, 78, 90, 95]

plt.plot(months, attendance, marker="o")

plt.title("Monthly Student Attendance")
plt.xlabel("Months")
plt.ylabel("Attendance (%)")

plt.show()

# pi chart with matplotlib 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataStudent .csv")

passed_count = (df["Marks"] >= 50).sum()
failed_count = (df["Marks"] < 50).sum()

labels = ["Passed", "Failed"]
sizes = [passed_count, failed_count]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Student Pass and Fail Percentage")

plt.show()



