import pandas as pd

schedule = pd.read_csv("output.csv")
print(schedule.sort_values("class_day"))