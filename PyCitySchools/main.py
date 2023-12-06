#***********************************************************************
# @file
#
# Module 4 Challenge
#
# @note None
#
# @warning  None
#
#  Created: December 5, 2023
#   Author: Emile Wirngo
#**********************************************************************/
#!/usr/bin/env python

# Dependencies and Setup
import pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")
print('school_data_to_load')
print(school_data_to_load)
print()

print('student_data_to_load')
print(student_data_to_load)
print()

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

print('school_data')
print(school_data)
print()

print('student_data')
print(student_data)
print()

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()

print('school_data_complete')
print(school_data_complete)
print()

print('school_data_complete.head()')
print(school_data_complete.head())
print()

# Calculate the total number of unique schools
school_count = len(school_data.index)
print('school_count')
print(school_count)
print()

## Calculate the total number of students
#student_count = 
#student_count
#
## Calculate the total budget
#total_budget = 
#total_budget
#
## Calculate the average (mean) math score
#average_math_score = 
#average_math_score
#
## Calculate the average (mean) reading score
#average_reading_score = 
#average_reading_score
#
## Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70)
#passing_math_count = school_data_complete[(school_data_complete["math_score"] >= 70)].count()["student_name"]
#passing_math_percentage = passing_math_count / float(student_count) * 100
#passing_math_percentage
#
## Calculate the percentage of students who passed reading (hint: look at how the math percentage was calculated)  
#passing_reading_count = 
#passing_reading_percentage = 
#
## Use the following to calculate the percentage of students that passed math and reading
#passing_math_reading_count = school_data_complete[
#    (school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70)
#].count()["student_name"]
#overall_passing_rate = passing_math_reading_count /  float(student_count) * 100
#overall_passing_rate
#
## Create a high-level snapshot of the district's key metrics in a DataFrame
#district_summary = 
#
## Formatting
#district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
#district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)
#
## Display the DataFrame
#district_summary
#
## Use the code provided to select all of the school types
#school_types = 
#
## Calculate the total student count per school
#per_school_counts = 
#
#