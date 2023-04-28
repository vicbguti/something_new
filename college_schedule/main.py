class_name, class_course, class_day, class_begin_hour, class_end_hour, class_professor = ("", "", "", "", "", "")

with open("schedule.txt") as file:
    with open("output.csv", "w") as output:
        output.write("class_name,class_course,class_day,class_begin_hour,class_end_hour,class_professor\n")
        lines = iter([x for x in file.readlines() if x != "\n"])
        for line in lines:
                while line[0] != "-":
                    while (line[0] != "[" and line[0] != "-"): 
                        if line.startswith(("Lunes","Martes","Miércoles","Jueves")):
                            class_day, class_begin_hour, class_end_hour = line.split("\t")

                            output.write("{},{},{},{},{},{}".format(class_name, class_course, class_day, class_begin_hour,
                                        class_end_hour.strip(), class_professor))
                            
                        else:
                            class_professor = line


                        
                        try:
                            line = next(lines)
                        except:
                            print("StopIteration handled succesfully")
                            line = "-"
                            
                    class_course = line[1:-2]
                    if line[0] != "-":
                        line = next(lines)
                class_name = line[1:-2]

    