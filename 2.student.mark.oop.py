# create class student
class Student :
    # contructor 
    def __init__(self , student_name ,student_id, student_dob)  : 
        self.name = student_name 
        self.id = student_id 
        self.dob = student_dob  
        # array scores and courses 
        self.scores = {}
        self.courses = []
        
    # add courses for student
    def add_course( self,course):
        self.courses.append(course)
    
    #input 
    def input_mark ( self , courses ,  mark) : 
        self.scores[courses ] = mark 
        
    # get     
    def get_mark ( self, courses  ): 
        return self.scores.get(courses,0)
# get mark of courses 

    
# create class courses 
class courses : 
    #contructor 
    def __init__(self , courses_id , courses_name):
        self.id = courses_id 
        self.name = courses_name 
        self.scores = {} 
    
    # input 
    def input_mark ( self , student , mark ) :
        self.scores[student] = mark 
    
    #get 
    def get_mark( self  , student ): # get mark of student 
        return self.scores.get(student , 0 ) 
    
    
# class school 
class school : 
    def __init__ ( self ) : 
        self.students = []
        self.courses = [] 
        self.score = []
    # create array student and courses 
    
    
    #add a sutdent 
    def add_student ( self , student_name , student_id , dob ) :
        self.students.append(Student(student_name , student_id , dob ))
    
        
    #add a courses 
    def add_courses ( self , student_id , courses_name , courses_id  ) : 
        new_course = courses( courses_id , courses_name )
        self.courses.append(new_course)
        
        for student in self.students : 
            if student.id == student_id : 
                student.add_course(new_course)
        
    # input mark 
    def input_mark(self, student_id, course_id, mark):
        for student in self.students:
            if student.id == student_id:
                for course in self.courses:
                    if course.id == course_id:
                        student.input_mark(course, mark)
                        course.input_mark(student, mark)
                        break
                break

    
    def list_student( self) : 
        for student in self.students :
            print(student.id , student.name, student.dob )


    def list_courses ( self):
        for courses in self.courses:
            print(courses.id , courses.name)    
            
    
    # print marks courses 
    def show_marks_for_courses( self , courses_id):
        for student in self.students : 
            for course in student.courses : 
                if course.id == courses_id: 
                    print(f" student {student.name} has score {student.get_mark(course)} in course {course.name}")
      
# main 
def main():
    schoo = school()
    while True:
        print("1. Add student")
        print("2. Add course")
        print("3. Input mark")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Exit")         
        
        opti = int ( input(" one choose is  : ")) 
        if opti == 1:
            num = int(input(" input amount of student : "))
            for _ in range ( num) : 
                name = input( " name is : ")
                id = input(" id is : ")
                dob = input("dob is : ")
                schoo.add_student(name , id , dob )
            
        if opti == 7 : 
            print (" okay you are exiting.........................")
            break 
        
        if opti == 2 : 
            student_id = input( " id student : ")
            name = input ("name course : ")
            id = input ( " id course: ")
            schoo.add_courses(student_id , name , id )
            
        if opti == 3 :
            student_id = input(" id of student : ")
            course_id = input ( " id of course : ")
            mark = float(input(" marks is : "))
            schoo.input_mark(student_id , course_id , mark ) 
 
            
        if opti == 4 : 
            schoo.list_student() 
        
        if opti == 5 : 
            schoo.list_courses()     
            
        if opti == 6 : 
            id = ( input(" courses id is : "))
            schoo.show_marks_for_courses (id)
        
if __name__ == "__main__":
    main()