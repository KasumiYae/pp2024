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
        mark.append(course_id , stu , mark_count)


def list_courses ():
    for couses_1 in courses :
        print (couses_1)
        

def list_students ():
    for student_1 in student :
        print(student_1)

def show_students_with_cousrses (courses ):
    for score in mark :
        if score[0] == courses : 
            print(f"student {mark[1]}  get score {mark[2]} in couses number {mark[0]} ")




# main 
def main (): 
    while True :
        print (" 1 . input number student  ")
        print (" 2 .  input information couses ")
        print (" 3 .  input mark of couses ")
        print ()
        
        
        print (" 0 : break ")
        
        option = int(input("choose : "))
        if option == 0 :
            print("ok , you break ")
            break 
        
        if option == 1 :
            print(" input  number student : " )
            number_student = input_number_students()
            print(number_student)
        






if __name__ == "__main__":
    main()