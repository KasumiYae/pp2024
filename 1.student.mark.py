student = []
courses = []
mark = []

# number of student 
def input_number_students():
    number = int(input("input number of students : "))
    return number 

# infor 
def input_infor_students():
    student_id = input("input student id :  ")
    name = input (" input name : ")
    DoB = input ( " input date of birth ")
    student.append(student_id , name , DoB) 

# number of coust 
def input_number_couse ():
    couse = int ( input ("input the number of couses : "))
    return couse 


# infor of course 
def input_infor_course():
    course_id = input("input id of course ")
    course_name = input("input name of course ")
    courses.append(course_id, course_name)

# input mark 
def input_mark (course_id):
    for stu in student :
        mark_count = float(input("input mark for student {stu[1]} in course {course_id}"))
        mark.append(stu , course_id , mark_count)

# main 
def main (): 
    while True :
        print (" 1 .  input information students ")
        print (" 2 .  input information couses ")
        print (" 3 .  input mark of couses ")
        print (" 0 : break ")
        
        option = int(input("choose :x "))
        if option == 0 :
            print("ok , you break ")
            break 
        
        if option == 1 :
            input_number_students
if __name__ == "__main__":
    main()