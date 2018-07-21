import numpy as np

calorie_stats = np.genfromtxt('cereal.csv',delimiter=',')
#print(calorie_stats)

print("Average calories of CrunchieMunchies: 60")

average_calories = np.mean(calorie_stats)
print("Average Calories from different brands:%.2f" %(average_calories))
print("Average amount of calories more than us:%.2f" %(average_calories - 60))

calorie_stats_sorted = np.sort(calorie_stats)
#print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print("Median calories of different brands: %.2f" %median_calories)

first_quater = np.percentile(calorie_stats,25)
print("Calorie count of 25th percentile of different brands:%.2f" %first_quater)

nth_percentile = np.percentile(calorie_stats,4)
print("Lowest percentile greater than 60 calories:%.2f" %nth_percentile)

percentage = np.mean(calorie_stats > 60)
print("Percentage of cereals having more than 60 calories:%.2f"%(percentage*100))

calorie_std = np.std(calorie_stats)
print("The standard deviation in the calorie stats of other brands:%.2f"%calorie_std)