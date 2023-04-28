import pandas as pd

df = pd.read_csv('output.csv')

classes = []

for _, row in df.iterrows():
    class_name = row['class_name']
    class_course = row['class_course']
    class_day = row['class_day']
    class_begin_hour = row['class_begin_hour']
    class_end_hour = row['class_end_hour']
    class_professor = row['class_professor']
    
    class_info = {'name': class_name,
                  'course': class_course,
                  'day': class_day,
                  'begin_hour': class_begin_hour,
                  'end_hour': class_end_hour,
                  'professor': class_professor}
                  
    classes.append(class_info)

schedule = []

for day in ['Lunes', 'Martes', 'Miércoles', 'Jueves']:
    daily_schedule = []
    added_classes = set()
    
    for class_info in classes:
        if class_info['day'] == day and class_info['name'] not in added_classes:
            daily_schedule.append(class_info)
            added_classes.add(class_info['name'])
            
    schedule.append(daily_schedule)

print(schedule[3])

# assuming you already have the `schedule` list from the previous example code

""" for i, option in enumerate(schedule):
    print("Option", i)
    for day in ['Lunes', 'Martes', 'Miércoles', 'Jueves']:
        df = pd.DataFrame(option)
        df = df[['name', 'course', 'begin_hour', 'end_hour', 'professor']]
        df.columns = ['Nombre de la materia', 'Código del curso', 'Hora de inicio', 'Hora de fin', 'Profesor']
    
        print(f'Schedule for {day}:')
        print(df)
        print('\n')
 """

# assuming you already have the `schedule` list from the previous example code

for i, day in enumerate(['Lunes', 'Martes', 'Miércoles', 'Jueves']):
    daily_schedule = schedule[i]
    df = pd.DataFrame(daily_schedule)
    df = df[['name', 'course', 'begin_hour', 'end_hour', 'professor']]
    df.columns = ['Nombre de la materia', 'Código del curso', 'Hora de inicio', 'Hora de fin', 'Profesor']
    
    print(f'Schedule for {day}:')
    print(df.iloc[:,:4])
    print('\n')
