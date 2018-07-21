# Crunchy_Munchy_project
This is the 5th project for the Codecademy Data Science intensive course. Here we use numpy's statistical analysis functions to analyze the data for the company.

# Overview
You work in marketing for a food company YummyCorps, which is developing a new kind of tasty, wholesome cereal called CrunchieMunchies. You want to demonstrate to consumers how healthy your cereal is in comparison to other leading brands, so you've dug up nutritional data on several different competitors. Your task is to use NumPy statistical calculations to analyze this data and prove that your CrunchieMunchies cereal is the healthiest choice for consumers.

# Objectives
1. Look over the cereal.csv file. This file contains the reported calorie amounts for different cereal brands. Load the data from the file and save it as calorie_stats.
2. There are 60 calories per serving of CrunchieMunchies. How much higher is the average calorie count of your competition? Save the answer to the variable average_calories and print the variable to the terminal to see the answer.
3. Does the average calorie count adequately reflect the distribution of the dataset? Let's sort the data and see. Sort the data and save the result to the variable calorie_stats_sorted. Print the sorted data to the terminal.
4. Looks like the majority of the cereals are higher than the mean. Let's see if the median is a better representative of the dataset. Calculate the median of the dataset and save your answer to median_calories. Print the median so you can see how it compares to the mean.
5. While the median demonstrates that at least half of our values are over 100 calories, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies. Calculate different percentiles and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable nth_percentile.
6. While the percentile shows us that the majority of the competition has a much higher calorie count, it's an awkward concept to use in marketing materials. Instead, let's calculate the percentage of cereals that have more than 60 calories per serving. Save your answer to the variable more_calories and print it to the terminal.
7. But one question is, how much variation exists in the dataset? Can we make the generalization that most cereals have around 100 calories or is the spread even greater? Calculate the amount of variation by finding the standard deviation. Save your answer to calorie_std and print to the terminal. How can we incorporate this value into our analysis?
8. Write a short paragraph that sums up your findings and how you think this data could be used to Yummy Corp's advantage when marketing CrunchieMunchies.

# Dependancies 
1. Numpy

# Additional comments
1. The data is imported from "cereal.csv" file.
2. The final objective is in "How this data can be used as an advantage.txt" file.
3. The rest of the objectives are solved in "code.py" file.
