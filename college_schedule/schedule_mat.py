import pandas as pd
import random

# Step 1: Read the CSV file
df = pd.read_csv('output.csv')

# Step 2: Group the data by class_name
class_dict = {}
for _, row in df.iterrows():
    class_name = row['class_name']
    class_course = row['class_course']
    if class_name not in class_dict:
        class_dict[class_name] = [class_course]
    else:
        class_dict[class_name].append(class_course)

# Step 3: Create an empty schedule dictionary
schedule = {}
days = ['Lunes', 'Martes', 'Miércoles', 'Jueves']
for day in days:
    schedule[day] = []

# Step 4: Generate a random schedule without repeating the same class_course in the same week
for class_name, class_courses in class_dict.items():
    random.shuffle(class_courses)  # shuffle the course list to get a random order
    used_courses = set()  # keep track of the used courses for this class_name in the current week
    for course in class_courses:
        # find a random day with no conflict for the class_name and course in the current week
        available_days = [day for day in days if not any(course == c[1] and class_name == c[0] for c in schedule[day])]
        if available_days:
            day = random.choice(available_days)
            # find a random time slot with no conflict for the class_name and course on the selected day
            available_slots = [(start, end) for start, end in zip(df['class_begin_hour'], df['class_end_hour']) 
                               if not any(start < c[3] < end or start < c[4] < end for c in schedule[day])
                               and not any(course == c[1] and class_name == c[0] for c in schedule[day])]
            if available_slots:
                start, end = random.choice(available_slots)
                professor = df[(df['class_name'] == class_name) & (df['class_course'] == course)]['class_professor'].values[0]
                schedule[day].append((class_name, course, day, start, end, professor))
                used_courses.add(course)
    # remove the used courses for this class_name from the list of available courses
    class_dict[class_name] = [c for c in class_courses if c not in used_courses]

# Step 5: Print the schedule
for day, classes in schedule.items():
    print(day)
    for c in classes:
        print(f"{c[0]} {c[1]} {c[3]}-{c[4]} {c[5]}")
