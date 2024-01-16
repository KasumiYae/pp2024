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
    student.append([student_id , name , DoB]) 

# number of coust 
def input_number_couse ():
    couse = int ( input ("input the number of couses : "))
    return couse 


# infor of course 
def input_infor_course():
    course_id = input("input id of course ")
    course_name = input("input name of course ")
    courses.append([course_id, course_name])

# input mark 
def input_mark (course_id):
    if not courses:
        print("you don't input courses id ")
        return 
    
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
    
    print (" MENU ")
    
    # dictonary
    option = {
        1 :  " input the amount of student " ,
        2 :  " input the information of student " , 
        3 :  " input the number of couses " , 
        4 :  " input the information of couses " , 
        5 :  " input the mark " , 
        6 :  " show list of student ",
        7 : " show list of couses " ,
        8 : " Show student marks for a given course ",
        9 : " exit menu " , 
    }
    
    array_option = []
    
    while True : 
        for op , choose in option.items() : 
            print(f"{op} , {choose}")

    
        options = int(input("put your choose : "))
        if options == 9 :
            print( " okay , you are exiting .............................................")
            break 
        
        if options == 1 : 
            num = input_number_students ()
            print (num)
            print (" ----------------------")

        if options == 2 : 
            if 'num' in locals(): 
                for _ in range(num):
                    infor = input_infor_students()
                    print (infor)
                    print("---------------------------------------------------------------------")
            else:
                print(" must put number of student , pls . ")
                print("-------------------------------------------------------------------")
            
        if options == 3 : 
            if 'num' in locals ():
                for _ in range(num): 
                    num_couses  = input_number_couse()
                    print(num_couses)
                    print("-------------------------------------------------------------------")
            else :  
                print(" must put number of student , pls . ")
                print("-------------------------------------------------------------------")
            
        if options == 4 :
            if 'num' in locals () and courses:
                for _ in range (num) : 
                    infor_couse = input_infor_course()
                    print ( infor_couse)
                    print("------------------------------------------------------------------------")
            else :  
                print(" must put number of student , pls . ")   
                print("-------------------------------------------------------------------")
        
                
        if options == 5 : 
            if 'num' in locals() and courses:
                for _ in range(num): 
                    for course in courses:
                        mark = input_mark(course[0])
                        print(mark)
                        print("-----------------------------------------------------------------------")
            else :  
                print("Must input number of students and courses first, please.")  
                print("--------------------------------------------------------------------------")
        
        
        if options == 6 : 
            if 'num' in locals() and student :
                list = list_students ()
                print(list)
                print("-------------------------------------------------------------------------")
            else:
                print(" you don't put number and information students ")
                print("--------------------------------------------------------------------------")

        if options == 7 : 
            if 'num' in locals() and courses :
                list = list_courses ()
                print(list)
                print("----------------------------------------------------------------------------")
            else : 
                print("you don't put information couses ")
                print("--------------------------------------------------------------------------")




if __name__ == "__main__":
    main()