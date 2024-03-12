import math
import numpy as np 

class Student :
    def __init__(self , student_name ,student_id, student_dob)  : 
        self.name = student_name 
        self.id = student_id 
        self.dob = student_dob  
        self.scores = {}
        self.courses = []
        
    def add_course( self,course):
        self.courses.append(course)
    
    def input_mark ( self , courses ,  mark) : 
        self.scores[courses ] = math.floor((mark * 10 ) / 10 )  
        
    def get_mark ( self, courses  ): 
        return self.scores.get(courses,0)
    
    def gpa (self , mark ) : 
        if self.scores : 
            return np.mean(list(self.scores.values())) 
        else: 
            return 0 
    
    def gpa_weight ( self, course_tinchi):
        if self.scores and course_tinchi : 
            total_tinchi = sum(course_tinchi.values())
            total_score  = sum(self.scores[course] for course in self.scores ) 
            return total_score / total_tinchi if total_tinchi else 0  
        else : 
            return 0
