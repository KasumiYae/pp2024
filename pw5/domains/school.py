from .student import Student
from .courses import courses

class school : 
    def __init__ ( self ) : 
        self.students = []
        self.courses = [] 
        self.score = []
    
    def add_student ( self , student_name , student_id , dob ) :
        self.students.append(Student(student_name , student_id , dob ))
    
    def add_courses ( self , student_id , courses_name , courses_id  ) : 
        new_course = courses( courses_id , courses_name )
        self.courses.append(new_course)
        
        for student in self.students : 
            if student.id == student_id : 
                student.add_course(new_course)
    
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
        
    def show_marks_for_courses( self , stdscr, courses_id):
        for student in self.students : 
            for course in student.courses : 
                if course.id == courses_id: 
                    stdscr.addstr(f" student {student.name} has score {student.get_mark(course)} in course {course.name}\n")
                    stdscr.refresh()
                    stdscr.getch()
    
    def sort_student(self) : 
        self.students.sort( key=lambda student:student.gpa , reverse=True)
