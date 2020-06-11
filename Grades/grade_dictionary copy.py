''' a function that, given a csv file of grades
creates a dictionary with keys for each student
and values of a list of grades'''
def create_grade_dict(file):
    # read the csv to a data variable
    data = ""
    with open(file, 'r') as f:
        data = f.read()

    # split up the data into a list of lines
    lines = data.split('\n')
    first_line = lines.pop(0) # first line is header info
    lines.pop(len(lines)-1) # last line is blank

    grade_dict = {}

    # loop through each line in the list
    for line in lines:
        # split the list on the comma
        entry = line.split(',')
        i = line.find(",")
        value = line[i + 1:]
        key = line [:i]
        grade_dict[key] = value

        '''
        Task 1:
        add each line to the grade_dict
        so that each key is a student's name
        and each value is a list of their grades as separate ints

        for example, the first entry should be in the dictionary as:
        'Albert':[90,85,89,91,80,88]
        '''
    return grade_dict




def get_average(scores):
    avg = sum(scores) / len(scores)
    return avg

    '''
    Task 2:
    complete this function that takes in a list of int scores
    as an input and calculates and returns the average score
    '''


# print the grade dictionary
grades = create_grade_dict("grades.csv")
for key, value in grades.items():
    print("Student:", key, "Grades:", value)




print('\n')
print("-----------------")

'''
Task 3:
write code to ask the user which student they would like to look up
if the specified student is found in the dictionary, use your function
to provide that student's average score
if that student is not found, print a message that says so
loop this so they can lookup multiple students
'''


def findStudent(Sname):
    for key, value in  grades:
        if Sname == key:
            return("Student:", key, "Average:", get_average(value))
        else:
            return("no name found")    



print(findStudent("Danica")



