# create class student
class student :
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
    def __int__ ( self ) : 
        self.students = []
        self.courses = [] 
    # create array student and courses 
    
    
    #add a sutdent 
    def add_student ( self , student_name , id , dob ) :
        self.students.append(student(student_name , id , dob ))
    
        
    #add a courses 
    def add_courses ( self , courses_name , id , ) : 
        self.courses.append(courses(courses_name , id))
        
        