import os   
import shutil # zip 
import curses
from domains.student import Student
from domains.courses import courses
from domains.school import school
from input import input_student, input_course, input_mark
from output import output_students, output_courses, output_marks_for_courses

#zip 
def zip_file():
    shutil.make_archive('student','zip','pw5')
    
def un_zip():
    if os.path.exists('student.zip'):    
        shutil.unpack_archive('student.zip','pw5')

def main(stdscr):
    un_zip()
    
    schoo = school()
    while True:
        stdscr.clear()
        stdscr.addstr("1. Add student\n")
        stdscr.addstr("2. Add course\n")
        stdscr.addstr("3. Input mark\n")
        stdscr.addstr("4. List students\n")
        stdscr.addstr("5. List courses\n")
        stdscr.addstr("6. Show marks for a course\n")
        stdscr.addstr("0. Exit\n")         

        opti = stdscr.getch()
        if opti == ord('1'):
            name, id, dob = input_student(stdscr)
            schoo.add_student(name , id , dob )

        if opti == ord('2'):
            student_id, name, id = input_course(stdscr)
            schoo.add_courses(student_id , name , id )

        if opti == ord('3'):
            student_id, course_id, mark = input_mark(stdscr)
            schoo.input_mark(student_id , course_id , mark )

        if opti == ord('4'):
            output_students(stdscr, schoo.students)

        if opti == ord('5'):
            output_courses(stdscr, schoo.courses)

        if opti == ord('6'):
            stdscr.addstr(" courses id is: ")
            stdscr.refresh()
            curses.echo()
            curses.nocbreak()
            course_id = stdscr.getstr().decode('utf-8')
            curses.noecho()
            curses.cbreak()
            output_marks_for_courses(stdscr, schoo.students, course_id)

        if opti == ord('0'):
            stdscr.addstr(" okay you are exiting.........................\n")
            stdscr.refresh()
            stdscr.getch()
            break

    zip_file()
if __name__ == "__main__":
    curses.wrapper(main)
