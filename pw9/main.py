import tkinter as tk
from tkinter import simpledialog
from domains.student import Student
from domains.courses import courses
from domains.school import school

def main():

    root = tk.Tk()
    root.withdraw()

    schoo = school.load()

    while True:
        opti = simpledialog.askstring("Option", "1. Add student\n2. Add course\n3. Input mark\n4. List students\n5. List courses\n6. Show marks for a course\n0. Exit\n")

        if opti == '1':
            name = simpledialog.askstring("Input", "student name: ")
            id = simpledialog.askstring("Input", "student id: ")
            dob = simpledialog.askstring("Input", "student dob: ")
            schoo.add_student(name , id , dob )

        if opti == '2':
            student_id = simpledialog.askstring("Input", "student ID: ")
            name = simpledialog.askstring("Input", "course name: ")
            id = simpledialog.askstring("Input", "course id: ")
            schoo.add_courses(student_id , name , id )

        if opti == '3':
            student_id = simpledialog.askstring("Input", "student id: ")
            course_id = simpledialog.askstring("Input", "course id: ")
            mark = simpledialog.askfloat("Input", "mark: ")
            schoo.input_mark(student_id , course_id , mark )

        if opti == '4':
            for student in schoo.students:
                print(f"{student.id} {student.name} {student.dob}")

        if opti == '5':
            for course in schoo.courses:
                print(f"{course.id} {course.name}")

        if opti == '6':
            course_id = simpledialog.askstring("Input", "course id: ")
            for student in schoo.students:
                for course in student.courses:
                    if course.id == course_id:
                        print(f" student {student.name} has score {student.get_mark(course)} in course {course.name}")

        if opti == '0':
            print("Exiting...")
            break

    schoo.save_thr()

if __name__ == "__main__":
    main()
