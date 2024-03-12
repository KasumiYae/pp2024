import tkinter as tk
from tkinter import simpledialog

def input_student(root):
    name = simpledialog.askstring("Input", "Student name: ", parent=root)
    id = simpledialog.askstring("Input", "Student ID: ", parent=root)
    dob = simpledialog.askstring("Input", "Student DOB: ", parent=root)
    return name, id, dob

def input_course(root):
    student_id = simpledialog.askstring("Input", "Student ID: ", parent=root)
    name = simpledialog.askstring("Input", "Course name: ", parent=root)
    id = simpledialog.askstring("Input", "Course ID: ", parent=root)
    return student_id, name, id

def input_mark(root):
    student_id = simpledialog.askstring("Input", "Student ID: ", parent=root)
    course_id = simpledialog.askstring("Input", "Course ID: ", parent=root)
    mark = simpledialog.askfloat("Input", "Mark: ", parent=root)
    return student_id, course_id, mark
