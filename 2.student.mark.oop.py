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
            if student.student_id == student_id:
                for course in self.courses:
                    if course.courses_id == course_id:
                        student.input_mark(course, mark)
                        course.input_mark(student, mark)
                        break
                break


    def list_student( self) : 
        for student in self.students :
            print(student.student_id , student.student_name, student.dob )


    def list_courses ( self):
        for courses in self.courses:
            print(courses.courses)        