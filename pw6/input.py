import curses
import os 

def input_student(stdscr):
    stdscr.addstr(" name is : ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    name = stdscr.getstr().decode('utf-8')
    curses.noecho()
    curses.cbreak()
    stdscr.addstr(" id is : ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    id = stdscr.getstr().decode('utf-8')
    curses.noecho()
    curses.cbreak()
    stdscr.addstr("dob is : ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    dob = stdscr.getstr().decode('utf-8')
    curses.noecho()
    curses.cbreak()
    return name, id, dob

    with open('/home/kasumi/code/python/pp2024/pw5/pw4' , 'a') as f :
        f.write(f'{name} , {id},{dob}\n')

def input_course(stdscr):
    stdscr.addstr(" id student : ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    student_id = stdscr.getstr().decode('utf-8')
    curses.noecho()
    curses.cbreak()
    stdscr.addstr("name course : ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    name = stdscr.getstr().decode('utf-8')
    curses.noecho()
    curses.cbreak()
    stdscr.addstr(" id course: ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    id = stdscr.getstr().decode('utf-8')
    curses.noecho()
    curses.cbreak()
    return student_id, name, id
    with open('/home/kasumi/code/python/pp2024/pw5/pw4','a' ) as f :
        f.write(f'{student_id} , {name} , { id} \n')


def input_mark(stdscr):
    stdscr.addstr(" id of student : ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    student_id = stdscr.getstr().decode('utf-8')
    curses.noecho()
    curses.cbreak()
    stdscr.addstr(" id of course : ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    course_id = stdscr.getstr().decode('utf-8')
    curses.noecho()
    curses.cbreak()
    stdscr.addstr(" marks is : ")
    stdscr.refresh()
    curses.echo()
    curses.nocbreak()
    mark = float(stdscr.getstr().decode('utf-8'))
    curses.noecho()
    curses.cbreak()
    return student_id, course_id, mark
    with open('/home/kasumi/code/python/pp2024/pw5/pw4','a') as f : 
        f.write(f'{student_id} , {course_id} , {mark} \n')
