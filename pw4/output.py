import curses

def output_students(stdscr, students):
    for student in students:
        stdscr.addstr(f"{student.id} {student.name} {student.dob}\n")
    stdscr.refresh()
    stdscr.getch()

def output_courses(stdscr, courses):
    for course in courses:
        stdscr.addstr(f"{course.id} {course.name}\n")
    stdscr.refresh()
    stdscr.getch()

def output_marks_for_courses(stdscr, students, course_id):
    for student in students:
        for course in student.courses:
            if course.id == course_id:
                stdscr.addstr(f" student {student.name} has score {student.get_mark(course)} in course {course.name}\n")
                stdscr.refresh()
                stdscr.getch()
