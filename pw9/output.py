import tkinter as tk
from tkinter import messagebox

def output_students(root, students):
    for student in students:
        messagebox.showinfo("Students", f"{student.id} {student.name} {student.dob}", parent=root)

def output_courses(root, courses):
    for course in courses:
        messagebox.showinfo("Courses", f"{course.id} {course.name}", parent=root)

def output_marks_for_courses(root, students, course_id):
    for student in students:
        for course in student.courses:
            if course.id == course_id:
                messagebox.showinfo("Marks", f" student {student.name} has score {student.get_mark(course)} in course {course.name}", parent=root)
