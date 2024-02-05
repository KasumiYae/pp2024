# create class student
class Student :
    # contructor 
    def __init__(self , student_name ,student_id, student_dob)  : 
        self.name = student_name 
        self.id = student_id 
        self.dob = student_dob  
        # array scores 
        self.scores = {}
    
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
    def input_markj ( self , student , mark ) :
        self.scores[student] = mark 
    
    #get 
    def get_mark( self  , student ): # get mark of student 
        return self.scores.get(student , 0 ) 
    
    
# class school 
class school : 
    def __init__ ( self ) : 
        self.students = []
        self.courses = [] 
    # create array student and courses 
    
    
    #add a sutdent 
    def add_student ( self , student_name , student_id , dob ) :
        self.students.append(Student(student_name , student_id , dob ))
    
        
    #add a courses 
    def add_courses ( self , courses_name , courses_id , ) : 
        self.courses.append(courses(courses_name , courses_id))
        
        
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
        for courses in self.courses : 
            if courses.id == courses_id :
                for student, scores  in courses.scores.iteam() : # student and mark in iteam  
                    print (f" the studentv { student.name}  have scores {scores} in the courses { courses.name}") 
      
      
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
            name = input(" name courses : ")
            id = input("id courses id : ")
            schoo.add_courses(name ,id , ) 
            
        if opti == 3 :
            name = input(" name of student : ")
            id = input ( " name of id : ")
            mark = float(input(" marks is : "))
            schoo.input_mark(name , id , mark ) 
            
        if opti == 4 : 
            schoo.list_student() 
        
        if opti == 5 : 
            schoo.list_courses()     
            
        if opti == 6 : 
            id = ( input(" courses id is : "))
            schoo.show_marks_for_courses (id)
        
if __name__ == "__main__":
    main()